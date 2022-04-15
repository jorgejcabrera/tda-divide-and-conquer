from unittest import TestCase

from rank.sort_service import SortService


class Test(TestCase):

    def test_merge_sort_with_should_work_ok(self):
        # given
        list = [3, 4, 2, 8, 6, 5]
        service = SortService()

        # when
        improvements = service.all_improvements_by_previous_position(list)

        #3
        # then
        self.assertTrue(1 == improvements.get(3))
        self.assertTrue(1 == improvements.get(4))
        self.assertTrue(1 == improvements.get(6))
        self.assertTrue(2 == improvements.get(8))



