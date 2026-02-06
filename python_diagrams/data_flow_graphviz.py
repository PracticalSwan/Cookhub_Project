from __future__ import annotations

from graphviz import Digraph
from pathlib import Path


def _init_graph(name: str) -> Digraph:
    g = Digraph(name, format="png")
    # Use curved splines so edge labels render attached (orthogonal 'ortho' detaches labels)
    g.attr(rankdir="TB", splines="ortho", nodesep="1.5", ranksep="3", overlap="false")
    g.attr("node", fontname="Arial")
    g.attr("edge", fontname="Arial")
    return g


def build_context_dfd() -> Digraph:
    g = _init_graph("DataFlow_Context")
    g.attr(label="Context DFD (Level 0)", labelloc="t")

    g.node("User", "User", shape="rectangle")
    g.node("Admin", "Admin", shape="rectangle")
    g.node("Contributor", "Contributor", shape="rectangle")
    g.node("Guest", "Guest (Pending/Suspended)", shape="rectangle")
    with g.subgraph() as roles:
        roles.attr(rank="same")
        roles.node("Admin", "Admin", shape="rectangle")
        roles.node("Contributor", "Contributor", shape="rectangle")
        roles.node("Guest", "Guest (Pending/Suspended)", shape="rectangle")
    g.node("System", "Recipe Sharing System", shape="circle")
    g.node("UsersDB", "Users DB", shape="cylinder")
    g.node("RecipesDB", "Recipes DB", shape="cylinder")
    g.node("ReviewsDB", "Reviews DB", shape="cylinder")
    g.node("SearchHistory", "Search History", shape="cylinder")
    g.node("DailyStats", "Daily Stats", shape="cylinder")
    g.node("ActivityLog", "Activity Log", shape="cylinder")
    g.node("SessionStore", "Session Store", shape="cylinder")

    with g.subgraph() as stores:
        stores.attr(rank="sink")
        stores.node("UsersDB", "Users DB", shape="cylinder")
        stores.node("RecipesDB", "Recipes DB", shape="cylinder")
        stores.node("ReviewsDB", "Reviews DB", shape="cylinder")
        stores.node("SearchHistory", "Search History", shape="cylinder")
        stores.node("DailyStats", "Daily Stats", shape="cylinder")
        stores.node("ActivityLog", "Activity Log", shape="cylinder")
        stores.node("SessionStore", "Session Store", shape="cylinder")

    g.edge("User", "System", xlabel="Credentials / Signup Data")
    g.edge("System", "User", xlabel="Auth Result / Session")
    g.edge("System", "Admin", xlabel="Auth Result / Session")
    g.edge("System", "Contributor", xlabel="Auth Result / Session")
    g.edge("System", "Guest", xlabel="Auth Result / Session")

    g.edge("Contributor", "System", xlabel="Browse/Search / View Detail")
    g.edge("System", "Contributor", xlabel="Recipe Listings / Detail")
    g.edge("Guest", "System", xlabel="Browse/Search / View Detail")
    g.edge("System", "Guest", xlabel="Recipe Listings / Detail")

    g.edge("Contributor", "System", xlabel="Likes, Favorites, Reviews")
    g.edge("System", "Contributor", xlabel="Updates / Confirmations")
    g.edge("Admin", "System", xlabel="Moderation / Stats Requests")
    g.edge("System", "Admin", xlabel="Results / Analytics")

    g.edge("System", "UsersDB")
    g.edge("UsersDB", "System")
    g.edge("System", "RecipesDB")
    g.edge("RecipesDB", "System")
    g.edge("System", "ReviewsDB")
    g.edge("ReviewsDB", "System")
    g.edge("System", "SearchHistory")
    g.edge("SearchHistory", "System")
    g.edge("System", "DailyStats")
    g.edge("DailyStats", "System")
    g.edge("System", "ActivityLog")
    g.edge("ActivityLog", "System")
    g.edge("System", "SessionStore")
    g.edge("SessionStore", "System")

    return g


def build_level1_dfd() -> Digraph:
    g = _init_graph("DataFlow_Level1")
    g.attr(label="Level 1 DFD", labelloc="t")

    g.node("U1", "User", shape="rectangle")
    g.node("A1", "Admin", shape="rectangle")
    g.node("C1", "Contributor", shape="rectangle")
    g.node("G1", "Guest (Pending/Suspended)", shape="rectangle")
    with g.subgraph() as roles:
        roles.attr(rank="same")
        roles.node("A1", "Admin", shape="rectangle")
        roles.node("C1", "Contributor", shape="rectangle")
        roles.node("G1", "Guest (Pending/Suspended)", shape="rectangle")

    for pid, label in [
        ("P1", "Authenticate & Register"),
        ("P2", "Session & Role Management"),
        ("P3", "Browse/Search Recipes"),
        ("P4", "View Recipe Detail"),
        ("P5", "Likes & Favorites"),
        ("P6", "Reviews & Ratings"),
        ("P6b", "Delete Review"),
        ("P7", "Create/Edit/Delete Recipe"),
        ("P8", "Profile Management"),
        ("P9", "Admin User Moderation"),
        ("P10", "Admin Recipe Moderation"),
        ("P11", "Analytics & Activity Logging"),
    ]:
        g.node(pid, label, shape="circle")

    g.node("D1", "Users DB", shape="cylinder")
    g.node("D2", "Recipes DB", shape="cylinder")
    g.node("D3", "Reviews DB", shape="cylinder")
    g.node("D4", "Search History", shape="cylinder")
    g.node("D5", "Daily Stats", shape="cylinder")
    g.node("D6", "Activity Log", shape="cylinder")
    g.node("D7", "Session Store", shape="cylinder")

    with g.subgraph() as stores:
        stores.attr(rank="sink")
        stores.node("D1", "Users DB", shape="cylinder")
        stores.node("D2", "Recipes DB", shape="cylinder")
        stores.node("D3", "Reviews DB", shape="cylinder")
        stores.node("D4", "Search History", shape="cylinder")
        stores.node("D5", "Daily Stats", shape="cylinder")
        stores.node("D6", "Activity Log", shape="cylinder")
        stores.node("D7", "Session Store", shape="cylinder")

    g.edge("U1", "P1", xlabel="Login/Signup Data")
    g.edge("P1", "U1", xlabel="Auth Result")
    g.edge("P1", "D1")
    g.edge("D1", "P1")
    g.edge("P1", "D6", xlabel="Signup Activity")
    g.edge("P1", "D5", xlabel="New User Stats")

    g.edge("P1", "P2", xlabel="Session Token")
    g.edge("P2", "D7")
    g.edge("D7", "P2")
    g.edge("P2", "U1", xlabel="Role/Status")
    g.edge("P2", "A1", xlabel="Admin")
    g.edge("P2", "C1", xlabel="Contributor")
    g.edge("P2", "G1", xlabel="Guest")
    g.edge("P2", "D5", xlabel="Active User Ping")

    g.edge("C1", "P3", xlabel="Search / Filter")
    g.edge("G1", "P3", xlabel="Search / Filter")
    g.edge("P3", "C1", xlabel="Recipe List")
    g.edge("P3", "G1", xlabel="Recipe List")
    g.edge("P3", "D2")
    g.edge("D2", "P3")
    g.edge("P3", "D4", xlabel="Save Search")
    g.edge("D4", "P3", xlabel="History Entries")
    g.edge("P3", "D4", xlabel="Clear History")

    g.edge("C1", "P4", xlabel="Recipe ID")
    g.edge("G1", "P4", xlabel="Recipe ID")
    g.edge("P4", "C1", xlabel="Detail")
    g.edge("P4", "G1", xlabel="Detail")
    g.edge("P4", "D2")
    g.edge("D2", "P4")
    g.edge("P4", "D5")

    g.edge("C1", "P5", xlabel="Like/Favorite")
    g.edge("P5", "D1")
    g.edge("D1", "P5")
    g.edge("P5", "D2")
    g.edge("D2", "P5")

    g.edge("C1", "P6", xlabel="Review Data")
    g.edge("P6", "D3")
    g.edge("D3", "P6")

    g.edge("C1", "P6b", xlabel="Delete Review")
    g.edge("P6b", "D3", xlabel="Remove Review")

    g.edge("C1", "P7", xlabel="Recipe Form")
    g.edge("P7", "D2")
    g.edge("D2", "P7")
    g.edge("P7", "D6")

    g.edge("C1", "P8", xlabel="Profile Updates")
    g.edge("P8", "D1")
    g.edge("D1", "P8")

    g.edge("A1", "P9", xlabel="User Actions")
    g.edge("P9", "D1")
    g.edge("D1", "P9")
    g.edge("P9", "D6")

    g.edge("A1", "P10", xlabel="Recipe Actions")
    g.edge("P10", "D2")
    g.edge("D2", "P10")
    g.edge("P10", "D6")

    g.edge("A1", "P11", xlabel="Stats Request")
    g.edge("P11", "D5")
    g.edge("D5", "P11")
    g.edge("P11", "D6")
    g.edge("D6", "P11")
    g.edge("P11", "A1", xlabel="Dashboard Stats")

    return g


def build_level2_dfd() -> Digraph:
    g = _init_graph("DataFlow_Level2")
    g.attr(label="Level 2 DFD (Full User + Admin Flows)", labelloc="t")

    g.node("U2", "User", shape="rectangle")
    g.node("A2", "Admin", shape="rectangle")
    g.node("C2", "Contributor", shape="rectangle")
    g.node("G2", "Guest (Pending/Suspended)", shape="rectangle")
    with g.subgraph() as roles:
        roles.attr(rank="same")
        roles.node("A2", "Admin", shape="rectangle")
        roles.node("C2", "Contributor", shape="rectangle")
        roles.node("G2", "Guest (Pending/Suspended)", shape="rectangle")
    for pid, label in [
        ("P10", "Validate Credentials"),
        ("P11", "Create Account"),
        ("P12", "Check Status & Role"),
        ("P13", "Start Session"),
        ("P14", "Browse/Search Recipes"),
        ("P15", "Save Search History"),
        ("P16", "View Recipe Detail"),
        ("P17", "Record View"),
        ("P18", "Toggle Like"),
        ("P19", "Toggle Favorite"),
        ("P20", "Add/Update Review"),
        ("P20b", "Delete Review"),
        ("P21a", "Validate Recipe Input"),
        ("P21", "Create/Edit Recipe"),
        ("P22", "Delete Own Recipe"),
        ("P23", "Update Profile"),
        ("P24", "Manage Users"),
        ("P25", "Manage Recipes"),
        ("P26", "View Dashboard Stats"),
        ("P27", "Review Activity Log"),
    ]:
        g.node(pid, label, shape="circle")

    g.node("D10", "Users DB", shape="cylinder")
    g.node("D11", "Recipes DB", shape="cylinder")
    g.node("D12", "Reviews DB", shape="cylinder")
    g.node("D13", "Search History", shape="cylinder")
    g.node("D14", "Daily Stats", shape="cylinder")
    g.node("D15", "Session Store", shape="cylinder")
    g.node("D16", "Activity Log", shape="cylinder")

    with g.subgraph() as stores:
        stores.attr(rank="sink")
        stores.node("D10", "Users DB", shape="cylinder")
        stores.node("D11", "Recipes DB", shape="cylinder")
        stores.node("D12", "Reviews DB", shape="cylinder")
        stores.node("D13", "Search History", shape="cylinder")
        stores.node("D14", "Daily Stats", shape="cylinder")
        stores.node("D15", "Session Store", shape="cylinder")
        stores.node("D16", "Activity Log", shape="cylinder")

    g.edge("U2", "P10", xlabel="Login Data")
    g.edge("P10", "D10", xlabel="User Lookup")
    g.edge("D10", "P10", xlabel="User Record")
    g.edge("P10", "U2", xlabel="Auth Result")

    g.edge("U2", "P11", xlabel="Signup Data")
    g.edge("P11", "D10", xlabel="New User (Pending)")
    g.edge("P11", "U2", xlabel="Account Created")
    g.edge("P11", "D16", xlabel="Signup Activity")
    g.edge("P11", "D14", xlabel="New User Stats")

    g.edge("P10", "P12", xlabel="User Status")
    g.edge("D10", "P12", xlabel="Status")
    g.edge("P12", "P13", xlabel="Admin/Contributor/Guest")
    g.edge("P13", "D15", xlabel="Session")
    g.edge("P13", "U2", xlabel="Session/Role")
    g.edge("P13", "A2", xlabel="Admin")
    g.edge("P13", "C2", xlabel="Contributor")
    g.edge("P13", "G2", xlabel="Guest")
    g.edge("P13", "D14", xlabel="Active User Ping")

    g.edge("C2", "P14", xlabel="Search / Filter")
    g.edge("G2", "P14", xlabel="Search / Filter")
    g.edge("P14", "D11", xlabel="Recipe List")
    g.edge("P14", "C2", xlabel="Recipe List")
    g.edge("P14", "G2", xlabel="Recipe List")
    g.edge("D12", "P14", xlabel="Rating Lookup")
    g.edge("P14", "P15", xlabel="Search Query")
    g.edge("P15", "D13", xlabel="Search Entry")

    g.edge("C2", "P16", xlabel="View Detail")
    g.edge("G2", "P16", xlabel="View Detail")
    g.edge("P16", "D11", xlabel="Recipe Data")
    g.edge("P16", "P17", xlabel="View Event")
    g.edge("P17", "D11", xlabel="Viewers Update")
    g.edge("P17", "D14", xlabel="View Stats")

    g.edge("C2", "P18", xlabel="Like")
    g.edge("P18", "D11", xlabel="Recipe Likes")

    g.edge("C2", "P19", xlabel="Favorite")
    g.edge("P19", "D10", xlabel="User Favorites")

    g.edge("C2", "P20", xlabel="Review")
    g.edge("P20", "D12", xlabel="Review Record")

    g.edge("C2", "P20b", xlabel="Delete Review")
    g.edge("P20b", "D12", xlabel="Remove Review")

    g.edge("C2", "P21a", xlabel="Recipe Form")
    g.edge("P21a", "C2", xlabel="Validation Errors")
    g.edge("P21a", "P21", xlabel="Valid Data")
    g.edge("P21", "D11", xlabel="Recipe Save")

    g.edge("C2", "P22", xlabel="Delete Recipe")
    g.edge("P22", "D11", xlabel="Remove Recipe")
    g.edge("P22", "D12", xlabel="Remove Reviews")
    g.edge("P22", "D10", xlabel="Clean Favorites")

    g.edge("C2", "P23", xlabel="Profile Updates")
    g.edge("P23", "D10", xlabel="Profile Save")

    g.edge("A2", "P24", xlabel="User Actions")
    g.edge("P24", "D10", xlabel="User Updates")
    g.edge("P24", "D16", xlabel="Admin Activity")

    g.edge("A2", "P25", xlabel="Recipe Actions")
    g.edge("P25", "D11", xlabel="Recipe Updates")
    g.edge("P25", "D16", xlabel="Admin Activity")

    g.edge("A2", "P26", xlabel="Stats Request")
    g.edge("P26", "D14", xlabel="Metrics")
    g.edge("P26", "A2", xlabel="Dashboard Stats")

    g.edge("A2", "P27", xlabel="Activity Review")
    g.edge("P27", "D16", xlabel="Activity Feed")
    g.edge("P27", "A2", xlabel="Activity Feed")

    return g


def main() -> None:
    out_dir = Path(__file__).parent / "out"
    out_dir.mkdir(parents=True, exist_ok=True)
    build_context_dfd().render(out_dir / "data_flow_context", cleanup=True)
    build_level1_dfd().render(out_dir / "data_flow_level1", cleanup=True)
    build_level2_dfd().render(out_dir / "data_flow_level2", cleanup=True)


if __name__ == "__main__":
    main()
