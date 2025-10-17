# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
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
        self.assertEqual(memo.content, "테스트 내용")

    def test_memo_str(self):
        """메모 __str__ 메서드 테스트"""
        memo = Memo.objects.create(
            user=self.user,
            title="테스트 메모",
            content="테스트 내용"
        )
        # Python 2/3 호환성을 고려하여 제목 포함 여부만 확인
        self.assertIn("테스트", str(memo))

    def test_memo_ordering(self):
        """메모 정렬 테스트 (최신순)"""
        memo1 = Memo.objects.create(
            user=self.user,
            title="메모1",
            content="내용1"
        )
        memo2 = Memo.objects.create(
            user=self.user,
            title="메모2",
            content="내용2"
        )
        memos = Memo.objects.all()
        self.assertEqual(memos[0], memo2)
        self.assertEqual(memos[1], memo1)

    def test_memo_user_relationship(self):
        """메모와 사용자 관계 테스트"""
        memo = Memo.objects.create(
            user=self.user,
            title="테스트 메모",
            content="테스트 내용"
        )
        self.assertEqual(memo.user.username, "testuser")
        self.assertEqual(self.user.memos.count(), 1)
        self.assertEqual(self.user.memos.first(), memo)
