const { cloud, db, COL, ok, fail } = require('../common/db')

exports.main = async (event) => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID
  const limit = Math.min(Number(event.limit) || 50, 200)

  const res = await db.collection(COL.students).where({ openid }).limit(1).get()
  if (!res.data.length) return ok({ records: [], summary: { recharge: 0, deduct: 0 } })

  const studentId = res.data[0]._id

  const recordsRes = await db
    .collection(COL.transactions)
    .where({ studentId })
    .orderBy('createdAt', 'desc')
    .limit(limit)
    .get()

  const records = recordsRes.data
  let recharge = 0
  let deduct = 0
  for (const r of records) {
    const amt = Number(r.amount) || 0
    if (amt > 0) recharge += amt
    else deduct += Math.abs(amt)
  }

  return ok({ records, summary: { recharge, deduct } })
}
