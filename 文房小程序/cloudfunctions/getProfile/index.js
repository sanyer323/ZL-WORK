const { cloud, db, COL, isAdmin, enrichStudent, todayStr, ok, fail } = require('../common/db')

exports.main = async () => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID

  const res = await db.collection(COL.students).where({ openid }).limit(1).get()
  const student = res.data.length ? enrichStudent(res.data[0]) : null

  let checkedInToday = false
  if (student) {
    const att = await db
      .collection(COL.attendance)
      .where({ openid, date: todayStr() })
      .limit(1)
      .get()
    checkedInToday = att.data.length > 0
  }

  return ok({
    student,
    isAdmin: await isAdmin(openid),
    checkedInToday
  })
}
