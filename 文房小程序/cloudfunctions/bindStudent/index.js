const { cloud, db, COL, enrichStudent, ok, fail } = require('../common/db')

exports.main = async (event) => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID
  const name = (event.name || '').trim()
  const phone = (event.phone || '').trim()

  if (!name) return fail('请输入姓名')

  const existing = await db.collection(COL.students).where({ openid }).limit(1).get()
  if (existing.data.length) {
    return ok({ student: enrichStudent(existing.data[0]) })
  }

  let target = null

  if (phone) {
    const byPhone = await db.collection(COL.students).where({ name, phone }).limit(5).get()
    target = byPhone.data.find(s => !s.openid) || null
  }

  if (!target) {
    const byName = await db.collection(COL.students).where({ name }).limit(20).get()
    target = byName.data.find(s => !s.openid) || null
  }

  if (!target) {
    return fail('未找到匹配的学员档案，请联系老师先在后台导入您的信息')
  }

  if (target.openid && target.openid !== openid) {
    return fail('该学员已被其他微信账号绑定')
  }

  await db.collection(COL.students).doc(target._id).update({
    data: {
      openid,
      phone: phone || target.phone || '',
      updatedAt: db.serverDate()
    }
  })

  const updated = await db.collection(COL.students).doc(target._id).get()
  return ok({ student: enrichStudent(updated.data) })
}
