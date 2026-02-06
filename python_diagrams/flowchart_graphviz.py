from __future__ import annotations

from graphviz import Digraph
from pathlib import Path


# Patch Digraph.edge so 'label' is converted to 'xlabel' for all instances.
# This ensures edge labels render correctly with orthogonal splines ('ortho').
_digraph_edge_orig = Digraph.edge
def _digraph_edge_with_xlabel(self, u, v, label=None, **kwargs):
    if label is not None:
        kwargs.setdefault('xlabel', label)
    return _digraph_edge_orig(self, u, v, **kwargs)
Digraph.edge = _digraph_edge_with_xlabel


def build_flowchart() -> Digraph:
    g = Digraph("ApplicationFlowchart", format="png")
    g.attr(rankdir="TB", splines="ortho", nodesep="1", ranksep="2.5", overlap="false")
    g.attr("node", shape="box", fontname="Arial")
    g.attr("edge", fontname="Arial")

    # Wrapper to use 'xlabel' for edge labels when using orthogonal splines.
    # Graphviz warns that 'label' doesn't work well with 'ortho'; 'xlabel'
    # places a separate label that renders correctly. Override g.edge
    # so existing calls with label= continue to work.
    _orig_edge = g.edge
    def _edge(u, v, label=None, **kwargs):
        if label is not None:
            kwargs.setdefault('xlabel', label)
        return _orig_edge(u, v, **kwargs)
    g.edge = _edge

    g.node("Start", "Start: User visits app", shape="oval")
    g.node("AuthAction", "Login or Sign Up?", shape="diamond")
    g.edge("Start", "AuthAction")

    # Login flow
    g.node("LoginStep1", "Enter email & password")
    g.node("LoginStep2", "Credentials valid?", shape="diamond")
    g.node("LoginError", "Show error")
    g.node("AdminCheck", "Admin credentials?", shape="diamond")
    g.node("AccountStatus", "Account status?", shape="diamond")
    g.edge("AuthAction", "LoginStep1", label="Login")
    g.edge("LoginStep1", "LoginStep2")
    g.edge("LoginStep2", "LoginError", label="No")
    g.edge("LoginError", "LoginStep1")
    g.edge("LoginStep2", "AdminCheck", label="Yes")
    g.edge("AdminCheck", "AdminEntry", label="Yes")
    g.edge("AdminCheck", "AccountStatus", label="No")
    # Account status determines routing for non-admin logins
    g.edge("AccountStatus", "GuestEntry", label="Suspended/Pending")
    g.edge("AccountStatus", "ContributorEntry", label="Active/Inactive")

    # Signup flow
    g.node("SignupStep1", "Enter registration details")
    g.node("SignupStep2", "Create user\n(role: user, status: pending)")
    g.node("SignupStep3", "Auto-login (Pending)")
    g.node("GuestEntry", "Enter Guest mode")
    g.edge("AuthAction", "SignupStep1", label="Sign Up")
    g.edge("SignupStep1", "SignupStep2")
    g.edge("SignupStep2", "SignupStep3")
    g.edge("SignupStep3", "GuestEntry")

    # Exit
    g.node("End", "End", shape="oval")
    g.edge("AuthAction", "End", label="Exit")

    # Role-based routing
    g.node("AdminEntry", "Enter Admin mode")
    g.node("ContributorEntry", "Enter Contributor mode")

    # Guest Mode subgraph
    with g.subgraph(name="cluster_guest") as guest:
        guest.attr(label="User (Guest mode)", color="gray50")
        guest.attr(rankdir="TB")
        guest.node("GuestAction", "Action?", shape="diamond", width="2", height="1.2", fontsize="14")
        guest.node("GuestBrowse", "View approved recipes")
        guest.node("GuestDetail", "Recipe detail page")
        guest.node("GuestBlock", "Show message:\nPending approval")
        guest.node("GuestLogout", "Clear session")

        guest.edge("GuestEntry", "GuestAction")
        guest.edge("GuestAction", "GuestBrowse", label="Browse/Search")
        guest.edge("GuestBrowse", "GuestAction")
        guest.edge("GuestAction", "GuestDetail", label="View Detail")
        guest.edge("GuestDetail", "GuestAction")
        guest.edge("GuestAction", "GuestBlock", label="Like/Save/Review/Create/Edit")
        guest.edge("GuestBlock", "GuestAction")
        guest.edge("GuestAction", "GuestLogout", label="Logout")

    # Contributor Mode subgraph
    with g.subgraph(name="cluster_contrib") as contrib:
        contrib.attr(label="User (Contributor mode)", color="gray50")
        contrib.attr(rankdir="TB")
        contrib.node("ContributorAction", "Action?", shape="diamond", width="2", height="1.2", fontsize="14")
        contrib.node("ContribBrowse", "View approved recipes")
        # storage nodes removed for flowchart simplicity
        contrib.node("ContribDetail", "Recipe detail page")
        contrib.node("ContribLike", "Toggle like")
        contrib.node("ContribSave", "Toggle favorite")
        # storage nodes removed for flowchart simplicity
        contrib.node("ContribReview", "Write/edit review")
        contrib.node("ContribProfile", "Edit profile")
        contrib.node("CreateStep1", "Fill recipe form")
        contrib.node("CreateStep2", "Form valid?", shape="diamond")
        contrib.node("CreateError", "Show validation error")
        contrib.node("CreateStep3", "Save recipe (Pending)")
        contrib.node("EditOwn", "Edit/Delete recipe")
        contrib.node("ContribLogout", "Clear session")

        contrib.edge("ContributorEntry", "ContributorAction")
        contrib.edge("ContributorAction", "ContribBrowse", label="Browse/Search")
        contrib.edge("ContribBrowse", "ContributorAction")
        contrib.edge("ContributorAction", "ContribDetail", label="View Detail")
        contrib.edge("ContribDetail", "ContributorAction")
        contrib.edge("ContributorAction", "ContribLike", label="Like")
        contrib.edge("ContribLike", "ContributorAction")
        contrib.edge("ContributorAction", "ContribSave", label="Save")
        contrib.edge("ContribSave", "ContributorAction")
        contrib.edge("ContributorAction", "ContribReview", label="Review")
        contrib.edge("ContribReview", "ContributorAction")
        contrib.edge("ContributorAction", "ContribProfile", label="Profile")
        contrib.edge("ContribProfile", "ContributorAction")
        contrib.edge("ContributorAction", "CreateStep1", label="Create Recipe")
        contrib.edge("CreateStep1", "CreateStep2")
        contrib.edge("CreateStep2", "CreateError", label="No")
        contrib.edge("CreateError", "CreateStep1")
        contrib.edge("CreateStep2", "CreateStep3", label="Yes")
        contrib.edge("CreateStep3", "ContributorAction")
        contrib.edge("ContributorAction", "EditOwn", label="Edit/Delete Own")
        contrib.edge("EditOwn", "ContributorAction")
        contrib.edge("ContributorAction", "ContribLogout", label="Logout")

    # Admin Mode subgraph
    with g.subgraph(name="cluster_admin") as admin:
        admin.attr(label="Admin mode", color="gray50")
        admin.attr(rankdir="TB")
        admin.node("AdminAction", "Admin Action?", shape="diamond", width="2", height="1.2", fontsize="14")
        admin.node("AdminStats", "View dashboard stats")
        # storage nodes removed for flowchart simplicity
        admin.node("AdminUsers", "Approve/Suspend/Delete users")
        admin.node("AdminRecipes", "Approve/Reject/Delete recipes")
        admin.node("AdminLog", "View activity log")
        admin.node("AdminLogout", "Clear session")

        admin.edge("AdminEntry", "AdminAction")
        admin.edge("AdminAction", "AdminStats", label="View Stats")
        admin.edge("AdminStats", "AdminAction")
        admin.edge("AdminAction", "AdminUsers", label="Manage Users")
        admin.edge("AdminUsers", "AdminAction")
        admin.edge("AdminAction", "AdminRecipes", label="Moderate Recipes")
        admin.edge("AdminRecipes", "AdminAction")
        admin.edge("AdminAction", "AdminLog", label="Review Activity")
        admin.edge("AdminLog", "AdminAction")
        admin.edge("AdminAction", "AdminLogout", label="Logout")

    g.edge("GuestLogout", "End")
    g.edge("ContribLogout", "End")
    g.edge("AdminLogout", "End")

    return g


def main() -> None:
    out_dir = Path(__file__).parent / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    g = build_flowchart()
    g.render(out_dir / "application_flowchart", cleanup=True)


if __name__ == "__main__":
    main()
