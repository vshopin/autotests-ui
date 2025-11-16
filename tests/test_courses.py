import pytest
from playwright.sync_api import expect, Page

BASE_PAGE = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_have_text('Courses')

    courses_list_empty_result = chromium_page_with_state.get_by_test_id(
        'courses-list-empty-view-title-text')
    expect(courses_list_empty_result).to_have_text('There is no results')

    courses_list_ikon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_list_ikon).to_be_visible()

    results_display = chromium_page_with_state.get_by_test_id(
        'courses-list-empty-view-description-text')
    expect(results_display).to_have_text(
        'Results from the load test pipeline will be displayed here'
    )
