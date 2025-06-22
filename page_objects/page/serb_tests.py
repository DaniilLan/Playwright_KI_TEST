import re
import time

import pyperclip

from core.utils.files_helpers.MMIL_data import calculate_all_matches, MMIL
from core.utils.files_helpers.QLESQ_data import QLESQ
from core.utils.files_helpers.SAN_data import *
from core.utils.files_helpers.OKO_data import OKO
from page_objects.base_page import BasePage


class LocatorsSERB:
    LINK_TEST_MMIL = '//span[text()="Методика многостороннего исследования личности (ММИЛ)"]'
    LINK_TEST_SAN = '//span[text()="Опросник «Самочувствие, Активность, Настроение» (САН)"]'
    LINK_TEST_IIG = '//span[text()="ЭЭГ-показатели для скрининга аффективной патологии"]'
    LINK_TEST_ITRAC = '//span[text()="ОСНОВНЫЕ ПАРАМЕТРЫ, АНАЛИЗИРУЕМЫЕ В ХОДЕ ОКУЛОГРАФИЧЕСКОГО ИССЛЕДОВАНИЯ (В СИСТЕМЕ Tobii Pro Lab)"]'
    LINK_TEST_OKO = '//span[text()="Опросник когнитивных ошибок (ОКО)"]'
    LINK_TEST_VRS = '//span[text()="Показатели вариабельности ритма сердца (ВРС)"]'
    LINK_TEST_DEBQ = '//span[text()="Голландский опросник пищевого поведения (DEBQ)"]'
    LINK_TEST_QLESQ = '//span[text()="Шкала качества жизни (Q-Les-Q)"]'

    BUTTON_NEXT_MANUAL = '//button[text()="Далее"]'
    ANSWER_YES = '//div[span[text()="Да"]]'
    ANSWER_NO = '//div[span[text()="Нет"]]'
    BUTTON_SAVE_ANSWER = '//button[text()="Сохранить"]'
    BUTTON_SAVE_CHANGE = '//button[span[text()="Сохранить"]]'
    LAST_PAGE_TEST = '//span[text()="377 из 377"]'
    SAN_ANSWER_1 = '//div[@class="CPYE"]//div[span[text()="3"]]'
    NOTIFICATION = '//div[text()="Тест пройден. За результатами обратитесь к врачу."]'

    FIRST_CARD_PATIENT = '//*[@id="root"]/div/div[1]/main/ul/li'
    PATIENT_OKO = '//li[.//span[text()="Тест ОКО "]]'
    PATIENT_MMIL = '//li[.//span[text()="Тест ММИЛ "]]'
    PATIENT_DEBQ = '//li[.//span[text()="Тест DEBQ "]]'
    PATIENT_QLESQ = '//li[.//span[text()="Тест Q-Les-Q "]]'

    ADD_EXAM = '//*[@id="root"]/div/div[1]/main/div[2]/div/button'
    CLUSTER_2 = '//div[span[text()="Психодиагностическое обследование"]]'
    CLUSTER_3 = '//div[span[text()="Нейрофизиологическое обследование"]]'
    BUTTON_SHARE_TEST = '//html/body/div[2]/div/div[3]/div[2]/button'

    CHAK_BOX_OKO = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[1]/div[3]/div/div'
    CHAK_BOX_SAN = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[3]/div[2]/div/div'
    CHAK_BOX_DEBQ = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[3]/div[4]/div/div'
    CHAK_BOX_QLESQ = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[3]/div[1]/div/div'
    CHAK_BOX_MMIL = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul[1]/div[1]/div/div'
    CHAK_BOX_VRS = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul/div[2]/div/div'
    CHAK_BOX_ITRAC = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul/div[1]/div/div'
    CHAK_BOX_IIG = '//html/body/div[2]/div/div[3]/div[2]/div/div[2]/ul/div[3]/div/div'
    CHAK_BOX_CHANGE_GENDER = "//html/body/div[2]/div/div[3]/div[3]/ul/li[1]/div/div/div"

    SHARE_LINK_TEST = '//html/body/div[2]/div/div[2]/div[2]/div/input'

    BUTTON_RESULT_TEST = '//*[@id="root"]/div/div[1]/main/div[2]/table/tbody/tr[1]/td[5]/div/button[2]'
    RESULT_TEST_OKO = "//span[text()='Опросник когнитивных ошибок (ОКО)']"
    RESULT_TEST_SAN = "//span[text()='Опросник «Самочувствие, Активность, Настроение» (САН)']"
    RESULT_TEST_MMIL = "//span[text()='Методика многостороннего исследования личности (ММИЛ)']"
    RESULT_TEST_DEBQ = "//span[text()='Голландский опросник пищевого поведения (DEBQ)']"

    GENDER_PATIENT = "//div[contains(@class, 'userCard-infoBlock')][.//span[text()='Пол']]/span[@class='patientInfo']"
    BUTTON_COPY_LINK_TEST = '//button[span[text()="Скопировать"]]'
    BUTTON_MENU_PATIENT = '//*[@id="root"]/div/div[1]/main/li/div/div[1]/div[2]'
    BUTTON_CHANGE = "//div[span[text()='Изменить']]"
    fourth_stage_QLESQ = "//div[@class='mFmQ']/span[text()='В целом, за последнюю неделю в какой степени Вы довольны…']"


class SerbPage(BasePage):

    def select_test_MMIL(self):
        self.click(LocatorsSERB.LINK_TEST_MMIL)

    def select_test_IIG(self):
        self.click(LocatorsSERB.LINK_TEST_IIG)

    def select_test_ITRAC(self):
        self.click(LocatorsSERB.LINK_TEST_ITRAC)

    def select_test_OKO(self):
        self.click(LocatorsSERB.LINK_TEST_OKO)

    def select_test_DEBQ(self):
        self.click(LocatorsSERB.LINK_TEST_DEBQ)

    def select_test_QLESQ(self):
        self.click(LocatorsSERB.LINK_TEST_QLESQ)

    def select_test_BPC(self):
        self.click(LocatorsSERB.LINK_TEST_VRS)

    def select_test_SAN(self):
        self.click(LocatorsSERB.LINK_TEST_SAN)

    def skip_manual(self):
        self.click(LocatorsSERB.BUTTON_NEXT_MANUAL)

    def click_answer_yes(self):
        self.click(LocatorsSERB.ANSWER_YES)

    def click_answer_no(self):
        self.click(LocatorsSERB.ANSWER_NO)

    def sending_answers_questions(self, answer, test):
        for answer_key in answer:
            if self.expect_visible_elements(LocatorsSERB.fourth_stage_QLESQ):
                class_name, text = QLESQ.transcript2[answer_key]
                self.click_by_answer(class_name, text)
                continue
            if test is MMIL:
                answer_key = answer_key[0]
            class_name, text = test.transcript[answer_key]
            self.click_by_answer(class_name, text)
            if self.expect_visible_elements(LocatorsSERB.BUTTON_SAVE_ANSWER):
                self.save_answer_in_test()

    def save_answer_in_test(self):
        self.click(LocatorsSERB.BUTTON_SAVE_ANSWER)

    def answer_oly_yes_until_last_question(self):
        while not self.expect_visible_elements(LocatorsSERB.LAST_PAGE_TEST):
            self.click_answer_yes()
            self.save_answer_in_test()

    def click_by_answer(self, class_name: str, text: str):
        locator = f'//div[@class="{class_name}"]//span[text()="{text}"]'
        self.click(locator)

    def expect_notification_completed_test(self):
        self.wait_visible_elements(LocatorsSERB.NOTIFICATION)
        self.expect_text(LocatorsSERB.NOTIFICATION, 'Тест пройден. За результатами обратитесь к врачу.')

    def create_test_go_to_test_SAN(self):
        self.click(LocatorsSERB.FIRST_CARD_PATIENT)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_2)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.CHAK_BOX_SAN)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def create_test_go_to_test_DEBQ(self):
        self.click(LocatorsSERB.PATIENT_DEBQ)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_2)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.CHAK_BOX_DEBQ)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def create_test_go_to_test_QLESQ(self):
        self.click(LocatorsSERB.PATIENT_QLESQ)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_2)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.CHAK_BOX_QLESQ)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def create_test_go_to_test_MMIL(self):
        self.click(LocatorsSERB.FIRST_CARD_PATIENT)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_2)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.CHAK_BOX_MMIL)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def create_test_go_to_test_BPC(self):
        self.click(LocatorsSERB.FIRST_CARD_PATIENT)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_3)
        self.click(LocatorsSERB.CHAK_BOX_VRS)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def create_test_go_to_test_IIG(self):
        self.click(LocatorsSERB.FIRST_CARD_PATIENT)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_3)
        self.click(LocatorsSERB.CHAK_BOX_IIG)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def create_test_go_to_test_ITREC(self):
        self.click(LocatorsSERB.FIRST_CARD_PATIENT)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_3)
        self.click(LocatorsSERB.CHAK_BOX_ITRAC)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def create_test_go_to_test_OKO(self):
        self.click(LocatorsSERB.PATIENT_OKO)
        self.click(LocatorsSERB.ADD_EXAM)
        self.click(LocatorsSERB.CLUSTER_2)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.CHAK_BOX_OKO)
        self.click(LocatorsSERB.BUTTON_SHARE_TEST)
        self.click(LocatorsSERB.BUTTON_COPY_LINK_TEST)
        link = pyperclip.paste()
        self.wait_time(1000)
        self.open(link)

    def go_to_page_doctor(self):
        self.open('http://192.168.7.35:8091/patients')

    def check_interpretation_for_test_CAN(self, answer):
        self.click(LocatorsSERB.FIRST_CARD_PATIENT)
        self.click(LocatorsSERB.BUTTON_RESULT_TEST)
        self.click(LocatorsSERB.CLUSTER_2)
        self.wait_load_state_networking()
        self.click(LocatorsSERB.RESULT_TEST_SAN)
        self.wait_load_state_networking()
        text_inter = ''
        if answer in (SAN.answers_1_min_30, SAN.answers_1_34, SAN.answers_1_60, SAN.answers_1_90, SAN.answers_1_96):
            text_inter = SAN.text_interpretation_1
        elif answer in (SAN.answers_2_102, SAN.answers_2_105, SAN.answers_2_120, SAN.answers_2_135, SAN.answers_2_138, SAN.answers_2_example):
            text_inter = SAN.text_interpretation_2
        elif answer in (SAN.answers_3_144, SAN.answers_3_150, SAN.answers_3_max_210):
            text_inter = SAN.text_interpretation_3
        fact_text = self.get_text('//html/body/div[2]/div/div[3]/div/div[3]/div/div[2]/span')
        assert fact_text == text_inter, (f'{fact_text} \n'
                                         f'!= {text_inter}\n'
                                         f'protokolId: \n'
                                         f'testId: \n')

    def delete_all_obs(self, FIO):
        self.click(f'//span[text()="{FIO}"]')
        button_delete = '//div[@class="passedTests-delete"]'
        while self.wait_visible_elements(button_delete):
            self.click(button_delete)
            self.click('//button[@class="button warning fullwidth"]')

    def fill_all_input_fields_IIG(self):
        text = '11111111'
        for i in range(4):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{i+5}]/input', text)
        for k in range(20):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{k+11}]/input', text)

    def fill_all_input_fields_ITRAC(self):
        text = '11111111'
        for i in range(4):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{i+5}]/input', text)
        for k in range(8):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{k+11}]/input', text)

    def fill_all_input_fields_BPC(self):
        text = '11111111'
        for i in range(4):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[{i+5}]/input', text)
        for k in range(20):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[11]/div[2]/div[{k+1}]/input', text)
        for j in range(20):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[12]/div[2]/div[{j+1}]/input', text)
        for e in range(3):
            self.fill_text(f'//*[@id="popap_window"]/div/div/div/div[2]/div[3]/div/div/div[2]/div[13]/div[2]/div[{e+1}]/input', text)

    def change_gender(self, target_gender):
        gender_labels = {
            'male': 'Мужской',
            'female': 'Женский'
        }
        self.click(LocatorsSERB.BUTTON_MENU_PATIENT)
        self.click(LocatorsSERB.BUTTON_CHANGE)
        self.wait_time(500)
        self.click(f"//label[@class='checkbox-label'][text()='{gender_labels[target_gender]}']")
        self.wait_time(500)
        self.click(LocatorsSERB.BUTTON_SAVE_CHANGE)

    def check_interpretation_for_test_OKO(self, answer):
        self.click(LocatorsSERB.PATIENT_OKO)
        self.click(LocatorsSERB.BUTTON_RESULT_TEST)
        self.click(LocatorsSERB.CLUSTER_2)
        self.wait_load_state_networking()
        self.click(LocatorsSERB.RESULT_TEST_OKO)
        self.wait_load_state_networking()
        if answer in (OKO.answer_all_limit, OKO.answer_all_max):
            for kay in OKO.interpretations:
                scale, true_interpretations = OKO.interpretations[kay]
                locator = f'//div[@class="testConclusion-container"][.//span[text()="{scale}"]]'
                text_inter = self.get_text(locator)
                assert text_inter == true_interpretations, (f"Ошибка текст "
                                                            f"\nФР: {text_inter}"
                                                            f"\n!= "
                                                            f"\nОР: {true_interpretations}")
        elif answer in (OKO.answer_0_min, OKO.answer_0_less_limit):
            for kay in OKO.interpretations:
                scale, _ = OKO.interpretations[kay]
                locator = f'//div[@class="testConclusion-container"][.//span[text()="{scale}"]]'
                self.expect_not_visible_elements(locator)
        else:
            raise ValueError(f"Неизвестный ответ: {answer}")

    def check_interpretation_for_test_MMIL(self, answer, gender):
        self.click(LocatorsSERB.PATIENT_MMIL)
        F_gender = self.get_text(LocatorsSERB.GENDER_PATIENT)
        gender_mapping = {
            'Мужской': 'male',
            'Женский': 'female'
        }
        if gender_mapping.get(F_gender) != gender:
            self.change_gender(gender)
        self.click(LocatorsSERB.BUTTON_RESULT_TEST)
        self.wait_after_appearance('//html/body/div[2]/div/div[4]/div')
        self.click(LocatorsSERB.CLUSTER_2)
        self.click(LocatorsSERB.RESULT_TEST_MMIL)
        self.wait_load_state_networking()

        data_result = calculate_all_matches(answer, gender)

        for scale, scale_data in data_result.items():
            if scale_data['interpretation'] != 'Не выводим':
                ui_scale_data = self.get_text(f'//div[div/div/span[text()="Шкала {scale.split("_")[1]}"]]')

                pattern = (
                    r"Шкала\s+"
                    r"(F|L|K|Hs|D|Hy|Pd|Mf|Pa|Pt|Sc|Ma|Si)"
                    r"\.?\s*"
                    r"([^=]*?)"
                    r"\s*"
                    r"(?:F|L|K|Hs|D|Hy|Pd|Mf|Pa|Pt|Sc|Ma|Si)"
                    r"\s*=\s*"
                    r"(\d+)"
                    r"\s*"
                    r"(.*)"
                )

                match = re.search(pattern, ui_scale_data)

                if not match:
                    raise ValueError(f"Не удалось распарсить текст интерпретации:\n{ui_scale_data}")

                scale_result = {
                    "Шкала": f'scale_{match.group(1)}',
                    "Название": f' {match.group(2).strip()}',
                    "Норма": match.group(3),
                    "Интерпретация": match.group(4).strip()
                }

                # Проверяем соответствие данных
                assert scale_result['Название'] == scale_data['scale_name'], (
                    f"Несоответствие названия шкалы {scale_result['Шкала']} (пол: {gender}):\n"
                    f"Фактическое: {scale_result['Название']}\n"
                    f"Ожидаемое: {scale_data['scale_name']}"
                )

                norm_key = 'Norm_M' if gender == 'male' else 'Norm_F'
                assert scale_result['Норма'] == str(scale_data[norm_key]), (
                    f"Несоответствие нормы для шкалы {scale_result['Шкала']} (пол: {gender}):\n"
                    f"Фактическое: {scale_result['Норма']}\n"
                    f"Ожидаемое: {scale_data[norm_key]}"
                )

                assert scale_result['Интерпретация'] == scale_data['interpretation'], (
                    f"Несоответствие интерпретации для шкалы {scale_result['Шкала']} (пол: {gender})\n "
                    f"C нормой Ф:{scale_result['Норма']} / О:{scale_data[norm_key]}:\n"
                    f"Фактическое: {scale_result['Интерпретация']}\n"
                    f"Ожидаемое: {scale_data['interpretation']}"
                )

    def check_interpretation_for_test_DEBQ(self):
        self.click(LocatorsSERB.PATIENT_DEBQ)
        self.click(LocatorsSERB.BUTTON_RESULT_TEST)
        self.click(LocatorsSERB.CLUSTER_2)
        self.wait_load_state_networking()
        self.click(LocatorsSERB.RESULT_TEST_DEBQ)
        self.wait_load_state_networking()


    def check_interpretation_for_test_QLESQ(self):
        self.click(LocatorsSERB.PATIENT_DEBQ)
        self.click(LocatorsSERB.BUTTON_RESULT_TEST)
        self.click(LocatorsSERB.CLUSTER_2)
        self.wait_load_state_networking()
        self.click(LocatorsSERB.RESULT_TEST_DEBQ)
        self.wait_load_state_networking()


