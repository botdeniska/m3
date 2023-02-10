from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext
from m3_ext.ui.fields.complex import ExtDictSelectField


class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'Password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )
        self.field__lastlogin = ext.ExtDateField(
            label=u'last login',
            name='lastlogin',
            anchor='100%',
            format="d.m.Y"
        )
        self.field__superstatus = ext.ExtCheckBox(
            label=u'superstatus',
            name='superstatus',
            anchor='100%'
        )
        self.field__username = ext.ExtStringField(
            label=u'Username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )
        self.field__firtname = ext.ExtStringField(
            label=u'firt name',
            name='first_name',
            anchor='100%'
        )
        self.field__lastname = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            anchor='100%'
        )
        self.field__email = ext.ExtStringField(
            label=u'email',
            name='email',
            anchor='100%'
        )
        self.field__staffstatus = ext.ExtCheckBox(
            label=u'staff status',
            name='staffstatus',
            anchor='100%'
        )
        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='active',
            anchor='100%',
            checked=True
        )
        self.field__datajoined = ext.ExtDateField(
            label=u'data joined',
            name='datajoined',
            anchor='100%',
            format="d.m.Y"
        )

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend(
            self.field__password,
            self.field__lastlogin,
            self.field__superstatus,
            self.field__username,
            self.field__firtname,
            self.field__lastname,
            self.field__email,
            self.field__staffstatus,
            self.field__active,
            self.field__datajoined,

        )

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):
    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()
        self.field__name = ext.ExtStringField(
            label=u'Name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )
        self.field__contenttype = ExtDictSelectField(
            label=u'content type',
            name='content_type',
            anchor='100%',
            url='rr',

        )

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            anchor='100%',
            allow_blank=False,
        )

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__contenttype,
            self.field__codename,
        ))

    def get_list_window_params(self, params, request, context):
        params = super(PermissionAddWindow, self).get_list_window_params(
            params, request, context)
        params.update({
            'title': u'Right things done by user: %s'
                     % request.user.username,
            'height': 800,
            'width': 600,
        })
        return params

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'
