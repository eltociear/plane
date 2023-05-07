# Module imports
from .base import BaseSerializer
from .issue import IssueFlatSerializer
from plane.db.models import Inbox, InboxIssue


class InboxSerializer(BaseSerializer):
    class Meta:
        model = Inbox
        fields = "__all__"
        read_only_fields = [
            "project",
            "workspace",
        ]


class InboxIssueSerializer(BaseSerializer):
    issue_detail = IssueFlatSerializer(source="issue", read_only=True)

    class Meta:
        model = InboxIssue
        fields = "__all__"
        read_only_fields = [
            "project",
            "workspace",
        ]
