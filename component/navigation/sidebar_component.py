import re

from playwright.sync_api import Page

from component.base_component import BaseComponent
from component.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, "logout")
        self.courses_list_item = SidebarListItemComponent(page, "courses")
        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard")

    def check_visible(self) -> None:
        self.logout_list_item.check_visible("Logout")
        self.courses_list_item.check_visible("Courses")
        self.dashboard_list_item.check_visible("Dashboard")

    def click_logout(self) -> None:
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    def click_courses(self) -> None:
        self.logout_list_item.navigate(re.compile(r".*/#/courses"))

    def click_dashboard(self) -> None:
        self.logout_list_item.navigate(re.compile(r".*/#/dashboard"))
