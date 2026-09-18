const { cloud, db, COL, enrichStudent, todayStr, ok, fail } = require('../common/db')

exports.main = async () => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID
  const date = todayStr()

  const res = await db.collection(COL.students).where({ openid }).limit(1).get()
  if (!res.data.length) return fail('请先绑定学员信息')

  const student = res.data[0]
  const classPrice = Number(student.classPrice) || 150
  const balance = Number(student.balance) || 0

  const existing = await db
    .collection(COL.attendance)
    .where({ openid, date })
    .limit(1)
    .get()

  if (existing.data.length) {
    return fail('今日已签到，请勿重复操作')
  }

  if (balance < classPrice) {
    return fail(`余额不足，当前 ¥${balance.toFixed(2)}，需 ¥${classPrice.toFixed(2)}`)
  }

  const newBalance = balance - classPrice
  const now = db.serverDate()

  await db.collection(COL.students).doc(student._id).update({
    data: {
      balance: newBalance,
      totalClasses: (Number(student.totalClasses) || 0) + 1,
      updatedAt: now
    }
  })

  await db.collection(COL.attendance).add({
    data: {
      studentId: student._id,
      openid,
      studentName: student.name,
      date,
      classPrice,
      amount: -classPrice,
      createdAt: now
    }
  })

  await db.collection(COL.transactions).add({
    data: {
      studentId: student._id,
      openid,
      type: 'deduct',
      amount: -classPrice,
      balanceAfter: newBalance,
      title: `${date} 上课扣费`,
      note: '签到自动扣费',
      createdAt: now
    }
  })

  const updated = await db.collection(COL.students).doc(student._id).get()
  return ok({ student: enrichStudent(updated.data) })
}
