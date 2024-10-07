from time import sleep

import pytest

from Configurations.readConfigurations import ReadConfiguration
from pageObject.policy_folders_page import PolicyFoldersPage


@pytest.mark.usefixtures("tear_down")
class TestPolicyFoldersPage:

    policy_folder_page_title = ReadConfiguration.get_title_name("policy_folders")

    def test_create_policy_folder(self, login_to_home_page):
        self.driver = login_to_home_page
        self.pfp = PolicyFoldersPage(self.driver)
        self.pfp.navigate_to_policy_folders_page()
        assert self.policy_folder_page_title in self.driver.title

