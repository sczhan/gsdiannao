from beidaqingniao.oop.supermarket.dao.admin_dao import AdminDao


class AdminService:

    def login(self, admin):
        admindao = AdminDao()
        return admindao.login(admin)