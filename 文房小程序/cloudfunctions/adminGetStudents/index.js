const { cloud, db, COL, isAdmin, enrichStudent, ok, fail } = require('../common/db')

exports.main = async (event) => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID
  const keyword = (event.keyword || '').trim().toLowerCase()

  if (!(await isAdmin(openid))) return fail('无管理员权限', 'FORBIDDEN')

  const res = await db.collection(COL.students).orderBy('name', 'asc').limit(500).get()
  let students = res.data.map(enrichStudent)

  if (keyword) {
    students = students.filter(s => {
      const name = (s.name || '').toLowerCase()
      const phone = (s.phone || '').toLowerCase()
      return name.includes(keyword) || phone.includes(keyword)
    })
  }

  return ok({ students })
}
