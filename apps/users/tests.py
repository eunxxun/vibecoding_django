# -*- coding: utf-8 -*-
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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


class UserViewTest(TestCase):
    """
    Users 뷰 테스트
    """

    def setUp(self):
        """테스트 설정"""
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123"
        )

    def test_register_view_get(self):
        """회원가입 페이지 조회 테스트"""
        response = self.client.get(reverse("users:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")

    def test_register_view_post_valid(self):
        """회원가입 성공 테스트"""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "testpass123",
            "password2": "testpass123"
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 302)  # 리다이렉트

    def test_register_view_post_duplicate_username(self):
        """중복 사용자명 회원가입 테스트"""
        data = {
            "username": "testuser",
            "email": "newemail@example.com",
            "password1": "testpass123",
            "password2": "testpass123"
        }
        response = self.client.post(reverse("users:register"), data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_login_view_get(self):
        """로그인 페이지 조회 테스트"""
        response = self.client.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_login_view_post_valid(self):
        """로그인 성공 테스트"""
        data = {
            "username": "testuser",
            "password": "testpass123"
        }
        response = self.client.post(reverse("users:login"), data)
        self.assertEqual(response.status_code, 302)  # 리다이렉트

    def test_login_view_post_invalid(self):
        """로그인 실패 테스트"""
        data = {
            "username": "testuser",
            "password": "wrongpassword"
        }
        response = self.client.post(reverse("users:login"), data)
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """로그아웃 테스트"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("users:logout"))
        self.assertEqual(response.status_code, 302)

    def test_profile_view_authenticated(self):
        """인증된 사용자 프로필 조회 테스트"""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/profile.html")

    def test_profile_view_unauthenticated(self):
        """미인증 사용자 프로필 조회 테스트 (리다이렉트)"""
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, 302)
