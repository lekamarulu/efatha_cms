from django.contrib import admin
from django.contrib import admin
from .models import (
    Member, MemberBranch, MemberBranchChurchPosition,
    MemberBranchDepartmentLeadership, MemberBranchMinistry,
    MemberEducation, MemberOccupation
)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("member_ref", "full_name", "gender", "email", "phone_number")
    search_fields = ("member_ref", "full_name", "email", "phone_number")
    list_filter = ("gender",)


@admin.register(MemberBranch)
class MemberBranchAdmin(admin.ModelAdmin):
    list_display = ("member_ref", "branch_ref", "start_date", "end_date")
    search_fields = ("member_ref", "branch_ref")


@admin.register(MemberBranchChurchPosition)
class MemberBranchChurchPositionAdmin(admin.ModelAdmin):
    list_display = ("member_ref", "branch_ref", "position", "start_date", "is_active")
    list_filter = ("is_active", "position")


@admin.register(MemberBranchDepartmentLeadership)
class MemberBranchDepartmentLeadershipAdmin(admin.ModelAdmin):
    list_display = ("member_ref", "branch_ref", "department", "leadership_role", "is_active")
    list_filter = ("is_active", "department")


@admin.register(MemberBranchMinistry)
class MemberBranchMinistryAdmin(admin.ModelAdmin):
    list_display = ("member_ref", "branch_ref", "ministry", "start_date", "end_date")


@admin.register(MemberEducation)
class MemberEducationAdmin(admin.ModelAdmin):
    list_display = ("member_ref", "level_ref", "institution_ref", "status")


@admin.register(MemberOccupation)
class MemberOccupationAdmin(admin.ModelAdmin):
    list_display = ("member_ref", "occupation_type", "company_name")
