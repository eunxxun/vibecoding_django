# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import Memo


class MemoModelTest(TestCase):
    """
    Memo 모델 테스트
    """

    def setUp(self):
        """테스트 설정"""
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )

    def test_memo_creation(self):
        """메모 생성 테스트"""
        memo = Memo.objects.create(
            user=self.user,
            title="테스트 메모",
            content="테스트 내용"
        )
        self.assertEqual(memo.title, "테스트 메모")
        self.assertEqual(memo.user, self.user)

    def test_memo_str(self):
        """메모 __str__ 메서드 테스트"""
        memo = Memo.objects.create(
            user=self.user,
            title="테스트 메모",
            content="테스트 내용"
        )
        self.assertEqual(str(memo), "테스트 메모")


class MemoViewTest(TestCase):
    """
    Memo 뷰 테스트
    """

    def setUp(self):
        """테스트 설정"""
        self.client = Client()
        self.user1 = User.objects.create_user(
            username="testuser1",
            email="test1@example.com",
            password="testpass123"
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            email="test2@example.com",
            password="testpass123"
        )
        self.memo1 = Memo.objects.create(
            user=self.user1,
            title="사용자1 메모",
            content="사용자1 내용"
        )
        self.memo2 = Memo.objects.create(
            user=self.user2,
            title="사용자2 메모",
            content="사용자2 내용"
        )

    def test_memo_list_view_unauthenticated(self):
        """미인증 사용자 메모 목록 조회 테스트 (리다이렉트)"""
        response = self.client.get(reverse("memos:memo_list"))
        self.assertEqual(response.status_code, 302)

    def test_memo_list_view_authenticated(self):
        """인증된 사용자 메모 목록 조회 테스트"""
        self.client.login(username="testuser1", password="testpass123")
        response = self.client.get(reverse("memos:memo_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "memos/memo_list.html")
        self.assertEqual(len(response.context["memos"]), 1)

    def test_memo_list_view_user_filtering(self):
        """메모 목록 사용자별 필터링 테스트"""
        self.client.login(username="testuser1", password="testpass123")
        response = self.client.get(reverse("memos:memo_list"))
        memos = response.context["memos"]
        for memo in memos:
            self.assertEqual(memo.user, self.user1)

    def test_memo_detail_view_owned(self):
        """소유한 메모 상세 조회 테스트"""
        self.client.login(username="testuser1", password="testpass123")
        response = self.client.get(reverse("memos:memo_detail", kwargs={"pk": self.memo1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["memo"], self.memo1)

    def test_memo_detail_view_not_owned(self):
        """소유하지 않은 메모 상세 조회 테스트 (404)"""
        self.client.login(username="testuser1", password="testpass123")
        response = self.client.get(reverse("memos:memo_detail", kwargs={"pk": self.memo2.pk}))
        self.assertEqual(response.status_code, 404)

    def test_memo_create_view_get(self):
        """메모 작성 페이지 조회 테스트"""
        self.client.login(username="testuser1", password="testpass123")
        response = self.client.get(reverse("memos:memo_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "memos/memo_form.html")

    def test_memo_create_view_post(self):
        """메모 작성 테스트"""
        self.client.login(username="testuser1", password="testpass123")
        data = {
            "title": "새 메모",
            "content": "새 메모 내용"
        }
        response = self.client.post(reverse("memos:memo_create"), data)
        self.assertEqual(Memo.objects.count(), 3)
        self.assertEqual(response.status_code, 302)

    def test_memo_update_view_owned(self):
        """소유한 메모 수정 테스트"""
        self.client.login(username="testuser1", password="testpass123")
        data = {
            "title": "수정된 메모",
            "content": "수정된 내용"
        }
        response = self.client.post(reverse("memos:memo_update", kwargs={"pk": self.memo1.pk}), data)
        self.memo1.refresh_from_db()
        self.assertEqual(self.memo1.title, "수정된 메모")
        self.assertEqual(response.status_code, 302)

    def test_memo_update_view_not_owned(self):
        """소유하지 않은 메모 수정 테스트 (404)"""
        self.client.login(username="testuser1", password="testpass123")
        data = {
            "title": "수정된 메모",
            "content": "수정된 내용"
        }
        response = self.client.post(reverse("memos:memo_update", kwargs={"pk": self.memo2.pk}), data)
        self.assertEqual(response.status_code, 404)

    def test_memo_delete_view_owned(self):
        """소유한 메모 삭제 테스트"""
        self.client.login(username="testuser1", password="testpass123")
        response = self.client.post(reverse("memos:memo_delete", kwargs={"pk": self.memo1.pk}))
        self.assertEqual(Memo.objects.count(), 1)
        self.assertEqual(response.status_code, 302)

    def test_memo_delete_view_not_owned(self):
        """소유하지 않은 메모 삭제 테스트 (404)"""
        self.client.login(username="testuser1", password="testpass123")
        response = self.client.post(reverse("memos:memo_delete", kwargs={"pk": self.memo2.pk}))
        self.assertEqual(Memo.objects.count(), 2)
        self.assertEqual(response.status_code, 404)
