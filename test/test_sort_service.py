from unittest import TestCase

from rank.sort_service import SortService
from test.player_record_factory import instance_one


class Test(TestCase):

    def test_merge_sort_with_should_work_ok_v2(self):
        # given
        list = instance_one()
        service = SortService()

        # when
        improvements = service.all_improvements_by_previous_position_v2(list)

        # 3
        # then
        self.assertTrue(1 == improvements.get("A"))
        self.assertTrue(1 == improvements.get("B"))
        self.assertTrue(1 == improvements.get("E"))
        self.assertTrue(2 == improvements.get("D"))



