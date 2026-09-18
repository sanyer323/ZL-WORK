const { cloud, db, COL, getSettings, isAdmin, enrichStudent, ok } = require('../common/db')

exports.main = async () => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID

  const settings = await getSettings()
  const admin = await isAdmin(openid)

  let student = null
  const res = await db.collection(COL.students).where({ openid }).limit(1).get()
  if (res.data.length) {
    student = enrichStudent(res.data[0])
  }

  return ok({
    openid,
    isAdmin: admin,
    student,
    studioName: settings.studioName || '文房书法'
  })
}
