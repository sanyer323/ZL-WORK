const { cloud, db, COL, enrichStudent, ok, fail } = require('../common/db')

exports.main = async (event) => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID
  const amount = Number(event.amount)

  if (!amount || amount <= 0) return fail('金额无效')

  const res = await db.collection(COL.students).where({ openid }).limit(1).get()
  if (!res.data.length) return fail('请先绑定学员信息')

  const student = res.data[0]
  const newBalance = (Number(student.balance) || 0) + amount
  const now = db.serverDate()

  await db.collection(COL.students).doc(student._id).update({
    data: {
      balance: newBalance,
      totalRecharged: (Number(student.totalRecharged) || 0) + amount,
      updatedAt: now
    }
  })

  await db.collection(COL.transactions).add({
    data: {
      studentId: student._id,
      openid,
      type: 'recharge',
      amount,
      balanceAfter: newBalance,
      title: event.channel === 'wxpay' ? '微信充值' : '账户充值',
      note: event.orderId || event.channel || '',
      createdAt: now
    }
  })

  const updated = await db.collection(COL.students).doc(student._id).get()
  return ok({ student: enrichStudent(updated.data) })
}
