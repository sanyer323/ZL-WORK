const { cloud, db, COL, isAdmin, enrichStudent, todayStr, ok, fail } = require('../common/db')

exports.main = async () => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID

  if (!(await isAdmin(openid))) return fail('无管理员权限', 'FORBIDDEN')

  const today = todayStr()
  const studentsRes = await db.collection(COL.students).limit(500).get()
  const students = studentsRes.data.map(enrichStudent)

  const attRes = await db.collection(COL.attendance).where({ date: today }).get()
  const txnRes = await db
    .collection(COL.transactions)
    .where({
      createdAt: db.command.gte(new Date(today + 'T00:00:00+08:00'))
    })
    .limit(500)
    .get()

  let todayRecharge = 0
  let todayDeduct = 0
  for (const t of txnRes.data) {
    const amt = Number(t.amount) || 0
    if (t.type === 'recharge') todayRecharge += amt
    if (t.type === 'deduct') todayDeduct += Math.abs(amt)
  }

  let totalBalance = 0
  let lowBalanceCount = 0
  for (const s of students) {
    totalBalance += s.balance
    if (s.balance < s.classPrice) lowBalanceCount += 1
  }

  return ok({
    overview: {
      todayCheckins: attRes.data.length,
      todayDeduct,
      todayRecharge,
      totalStudents: students.length,
      totalBalance,
      lowBalanceCount
    }
  })
}
