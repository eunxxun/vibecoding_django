# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    """
    User 모델 테스트
    """

    def test_user_creation(self):
        """사용자 생성 테스트"""
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("testpass123"))

    def test_duplicate_username(self):
        """중복 사용자명 테스트"""
        User.objects.create_user(
            username="testuser",
            email="test1@example.com",
            password="testpass123"
        )
        with self.assertRaises(Exception):
            User.objects.create_user(
                username="testuser",
                email="test2@example.com",
                password="testpass123"
            )

    def test_user_str(self):
        """User __str__ 메서드 테스트"""
        user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )
        self.assertEqual(str(user), "testuser")
