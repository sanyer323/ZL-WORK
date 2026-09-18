const { cloud, db, COL, isAdmin, ok, fail } = require('../common/db')

exports.main = async (event) => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID
  const month = event.month || ''

  if (!(await isAdmin(openid))) return fail('无管理员权限', 'FORBIDDEN')
  if (!/^\d{4}-\d{2}$/.test(month)) return fail('月份格式应为 YYYY-MM')

  const start = new Date(`${month}-01T00:00:00+08:00`)
  const end = new Date(start)
  end.setMonth(end.getMonth() + 1)

  const attRes = await db
    .collection(COL.attendance)
    .where({
      createdAt: db.command.gte(start).and(db.command.lt(end))
    })
    .limit(1000)
    .get()

  const txnRes = await db
    .collection(COL.transactions)
    .where({
      createdAt: db.command.gte(start).and(db.command.lt(end))
    })
    .limit(1000)
    .get()

  let deductTotal = 0
  let rechargeTotal = 0
  const byStudentMap = {}

  for (const a of attRes.data) {
    const name = a.studentName || '未知'
    const amt = Math.abs(Number(a.amount) || Number(a.classPrice) || 0)
    deductTotal += amt
    if (!byStudentMap[name]) byStudentMap[name] = { name, count: 0, amount: 0 }
    byStudentMap[name].count += 1
    byStudentMap[name].amount += amt
  }

  for (const t of txnRes.data) {
    const amt = Number(t.amount) || 0
    if (t.type === 'recharge') rechargeTotal += amt
  }

  const byStudent = Object.values(byStudentMap).sort((a, b) => b.count - a.count)

  return ok({
    stats: {
      month,
      checkinCount: attRes.data.length,
      deductTotal,
      rechargeTotal,
      byStudent
    }
  })
}
