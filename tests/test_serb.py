import time
from tabnanny import check

import pytest

from core.utils.files_helpers.DEBQ_data import DEBQ
from core.utils.files_helpers.QLESQ_data import QLESQ
from core.utils.files_helpers.SAN_data import SAN
from core.utils.files_helpers.MMIL_data import MMIL
from core.utils.files_helpers.OKO_data import OKO


class TestSerb:
    # @pytest.mark.parametrize('answer', [
    #                                             SAN.answers_1_34,
    #                                             SAN.answers_1_60,
    #                                             SAN.answers_1_90,
    #                                             SAN.answers_1_96,
    #                                             SAN.answers_2_102,
    #                                             SAN.answers_2_105,
    #                                             SAN.answers_2_120,
    #                                             SAN.answers_2_135,
    #                                             SAN.answers_2_138,
    #                                             SAN.answers_3_144,
    #                                             SAN.answers_3_150,
    #                                             SAN.answers_2_example,
    #                                             SAN.answers_3_max_210,
    #                                             SAN.answers_1_min_30,
    #                                             ],
    #                          ids=[
    #                              "answers_1_34",
    #                              "answers_1_60",
    #                              "answers_1_90",
    #                              "answers_2_102",
    #                              "answers_2_105",
    #                              "answers_2_120",
    #                              "answers_2_135",
    #                              "answers_2_138",
    #                              "answers_3_144",
    #                              "answers_3_150",
    #                              "answers_2_example",
    #                              "answers_2_120",
    #                              "answers_3_max_210",
    #                              "answers_1_min_30",
    #                          ]
    #                          )
    # def test_CAH(self, auth_serb, answer):
    #     auth_serb.create_test_go_to_test_SAN()
    #     auth_serb.select_test_SAN()
    #     auth_serb.skip_manual()
    #     auth_serb.sending_answers_questions(answer, SAN)
    #     auth_serb.expect_notification_completed_test()
    #     auth_serb.go_to_page_doctor()
    #     auth_serb.check_interpretation_for_test_SAN(answer)

    @pytest.mark.parametrize('gender', ['male', 'female'])
    @pytest.mark.parametrize('answer', [
                                        MMIL.answer_test_yes,
                                        MMIL.answer_test_no,
                                        MMIL.answer_BAA1_random,
                                        MMIL.answer_BAA2_random,
                                        MMIL.answer_COK_random,
                                        MMIL.answer_KOEA1_random,
                                        ],
                             ids=[
                                 "answer_test_yes",
                                 "answer_test_no",
                                 "answer_BAA1_random",
                                 "answer_BAA2_random",
                                 "answer_COK_random",
                                 "answer_KOEA1_random",
                             ]
                             )
    def test_MMIL(self, auth_serb, answer, gender):
        auth_serb.create_test_go_to_test_MMIL()
        auth_serb.select_test_MMIL()
        auth_serb.skip_manual()
        auth_serb.sending_answers_questions(answer, MMIL)
        auth_serb.expect_notification_completed_test()
        auth_serb.go_to_page_doctor()
        auth_serb.check_interpretation_for_test_MMIL(answer, gender)

    # def test_IIG(self, auth_serb):
    #     auth_serb.create_test_go_to_test_IIG()
    #     auth_serb.select_test_IIG()
    #     auth_serb.skip_manual()
    #     auth_serb.fill_all_input_fields_IIG()
    #     auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()
    #
    # def test_VRS(self, auth_serb):
    #     auth_serb.create_test_go_to_test_VRS()
    #     auth_serb.select_test_VRS()
    #     auth_serb.fill_all_input_fields_VRS()
    #     auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()
    #
    # def test_ITRAC(self, auth_serb):
    #     auth_serb.create_test_go_to_test_ITREC()
    #     auth_serb.select_test_ITRAC()
    #     auth_serb.fill_all_input_fields_ITRAC()
    #     auth_serb.save_answer_in_test()
    #     auth_serb.expect_notification_completed_test()

    # def test_delete(self, auth_serb):
    #     auth_serb.delete_all_obs('Ланцов Даниил Андреевич')

    # @pytest.mark.parametrize('answer', [
    #                                     OKO.answer_0_min,
    #                                     OKO.answer_all_max,
    #                                     OKO.answer_0_less_limit,
    #                                     OKO.answer_all_limit,
    #                                     ],
    #                          ids=[
    #                              "answer_0_min",
    #                              "answer_all_max",
    #                              "answer_0_less_limit",
    #                              "answer_all_limit",
    #                          ]
    #                          )
    # def test_OKO(self, auth_serb, answer):
    #     auth_serb.create_test_go_to_test_OKO()
    #     auth_serb.select_test_OKO()
    #     auth_serb.skip_manual()
    #     auth_serb.sending_answers_questions(answer, OKO)
    #     auth_serb.expect_notification_completed_test()
    #     auth_serb.go_to_page_doctor()
    #     auth_serb.check_interpretation_for_test_OKO(answer)

    # @pytest.mark.parametrize('answer', [
    #                                     DEBQ.answer_max_norma,
    #                                     # DEBQ.answer_min_norma,
    #                                     # DEBQ.answer_border_higher,
    #                                     # DEBQ.answer_border_lower,
    #                                     # DEBQ.answer_higher1,
    #                                     # DEBQ.answer_higher2,
    #                                 ],
    #                          ids=[
    #                              "answer_max_norma",
    #                              # "answer_min_norma",
    #                              # "answer_border_higher",
    #                              # "answer_border_lower",
    #                              # "answer_higher1",
    #                              # "answer_higher2",
    #                          ]
    #                          )
    # def test_DEBQ(self, auth_serb, answer):
    #     auth_serb.create_test_go_to_test_DEBQ()
    #     auth_serb.select_test_DEBQ()
    #     auth_serb.skip_manual()
    #     auth_serb.sending_answers_questions(answer, DEBQ)
    #     auth_serb.expect_notification_completed_test()
    #     auth_serb.go_to_page_doctor()
    #     auth_serb.check_interpretation_for_test_DEBQ()

    # @pytest.mark.parametrize('answer', [
    #                                     QLESQ.answer_max_norma,
    #                                     QLESQ.answer_min_norma,
    #                                     QLESQ.answer_border_higher,
    #                                     QLESQ.answer_border_lower,
    #                                     QLESQ.answer_higher1,
    #                                     QLESQ.answer_higher2,
    #                                 ],
    #                          ids=[
    #                              "answer_max_norma",
    #                              "answer_min_norma",
    #                              "answer_border_higher",
    #                              "answer_border_lower",
    #                              "answer_higher1",
    #                              "answer_higher2",
    #                          ]
    #                          )
    # def test_QLESQ(self, auth_serb, answer):
    #     auth_serb.create_test_go_to_test_QLESQ()
    #     auth_serb.select_test_QLESQ()
    #     auth_serb.skip_manual()
    #     auth_serb.sending_answers_questions(answer, QLESQ)
    #     auth_serb.expect_notification_completed_test()
    #     auth_serb.go_to_page_doctor()
    #     auth_serb.check_interpretation_for_test_QLESQ()