const { cloud, db, COL, isAdmin, ok, fail } = require('../common/db')

/**
 * 导入学员档案（管理员）
 * event.students: [{ name, phone, balance, classPrice, note, totalClasses }]
 * event.replace: 为 true 时清空未绑定 openid 的同名旧记录后再导入
 */
exports.main = async (event) => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID

  if (!(await isAdmin(openid))) return fail('无管理员权限', 'FORBIDDEN')

  const list = event.students || []
  if (!list.length) return fail('没有可导入的数据')

  const settingsRes = await db.collection(COL.settings).limit(1).get()
  const defaultPrice = settingsRes.data[0]?.defaultClassPrice || 150

  let imported = 0
  let skipped = 0
  const now = db.serverDate()

  for (const row of list) {
    const name = (row.name || '').trim()
    if (!name) {
      skipped += 1
      continue
    }

    const phone = (row.phone || '').trim()
    const balance = Number(row.balance)
    const classPrice = Number(row.classPrice) || defaultPrice
    const totalClasses = Number(row.totalClasses) || 0
    const note = row.note || ''

    const existing = await db
      .collection(COL.students)
      .where(phone ? { name, phone } : { name })
      .limit(5)
      .get()

    const bound = existing.data.find(s => s.openid)
    if (bound) {
      await db.collection(COL.students).doc(bound._id).update({
        data: {
          balance: Number.isFinite(balance) ? balance : bound.balance,
          classPrice,
          note: note || bound.note,
          updatedAt: now
        }
      })
      imported += 1
      continue
    }

    const unbound = existing.data.find(s => !s.openid)
    if (unbound) {
      await db.collection(COL.students).doc(unbound._id).update({
        data: {
          balance: Number.isFinite(balance) ? balance : unbound.balance,
          classPrice,
          totalClasses,
          note,
          updatedAt: now
        }
      })
      imported += 1
      continue
    }

    await db.collection(COL.students).add({
      data: {
        name,
        phone,
        balance: Number.isFinite(balance) ? balance : 0,
        classPrice,
        totalClasses,
        totalRecharged: Number.isFinite(balance) ? balance : 0,
        note,
        status: 'active',
        createdAt: now,
        updatedAt: now
      }
    })
    imported += 1
  }

  return ok({ imported, skipped, total: list.length })
}
