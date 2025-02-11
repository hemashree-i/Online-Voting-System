from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(DistrictModel)
admin.site.register(LocalbodyModel)
admin.site.register(WardModel)
admin.site.register(PollingstationModel)
admin.site.register(UserRegisterModel)
admin.site.register(UserLoginModel)
admin.site.register(VoterAddModel)
admin.site.register(AddSocialModel)
admin.site.register(ProbabilityModel)
admin.site.register(ExcelModel)
admin.site.register(CommentModel)
admin.site.register(SuperMemberModel)
admin.site.register(PresidentModel)
admin.site.register(AdminModel)
admin.site.register(ReportIssueModel)
admin.site.register(IssueReplyModel)
admin.site.register(AssignTaskModel)

