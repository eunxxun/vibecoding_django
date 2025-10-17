# 메모짱 (Memojjang)

당신의 생각을 간편하게 기록하고 관리하세요. Django 기반의 간단하고 안전한 메모 웹 애플리케이션입니다.

## 🎯 주요 기능

- ✍️ **메모 작성**: 간단한 인터페이스로 빠르게 메모 작성
- 📝 **메모 관리**: 메모 목록 조회, 수정, 삭제 (사용자별 격리)
- 🔐 **사용자 인증**: 안전한 회원가입 및 로그인
- 👤 **사용자 프로필**: 사용자 정보 관리
- 🎨 **반응형 디자인**: Bootstrap을 이용한 모던한 UI

## 📋 시스템 요구사항

- Python 2.7 (또는 Python 3.x)
- Django 1.7
- SQLite3 (기본 데이터베이스)

## 🚀 설치 및 실행

### 1. 저장소 클론

```bash
git clone https://github.com/eunxxun/vibecoding_django.git
cd vibecoding_django
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 마이그레이션

```bash
python manage.py migrate
```

### 4. 슈퍼유저 생성 (관리자 계정)

```bash
python manage.py createsuperuser
```

### 5. 개발 서버 실행

```bash
python manage.py runserver
```

서버가 실행되면 http://127.0.0.1:8000/ 에서 애플리케이션에 접근할 수 있습니다.

## 📖 사용 방법

### 홈페이지
- 기본 주소: http://127.0.0.1:8000/

### 회원가입
- 주소: http://127.0.0.1:8000/users/register/
- 사용자명, 이메일, 비밀번호를 입력하여 가입

### 로그인
- 주소: http://127.0.0.1:8000/users/login/
- 사용자명 또는 이메일과 비밀번호로 로그인

### 메모 관리
- 메모 목록: http://127.0.0.1:8000/memos/
- 메모 작성: http://127.0.0.1:8000/memos/create/
- 메모 상세: http://127.0.0.1:8000/memos/{id}/
- 메모 수정: http://127.0.0.1:8000/memos/{id}/update/
- 메모 삭제: http://127.0.0.1:8000/memos/{id}/delete/

### 관리자 페이지
- 주소: http://127.0.0.1:8000/admin/
- 슈퍼유저 계정으로 로그인하여 사용자 및 메모 관리

## 🏗️ 프로젝트 구조

```
vibecoding_django/
├── memojjang/                  # 메인 프로젝트 설정
│   ├── __init__.py
│   ├── settings.py            # Django 설정
│   ├── urls.py                # URL 라우팅
│   ├── views.py               # 홈페이지 뷰
│   └── wsgi.py
├── apps/                      # Django 애플리케이션
│   ├── users/                 # 사용자 앱
│   │   ├── models.py          # UserProfile 모델
│   │   ├── views.py           # 사용자 관련 뷰
│   │   ├── forms.py           # 사용자 폼
│   │   ├── urls.py            # 사용자 URL
│   │   ├── admin.py           # 관리자 설정
│   │   └── tests.py           # 테스트
│   └── memos/                 # 메모 앱
│       ├── models.py          # Memo 모델
│       ├── views.py           # 메모 관련 뷰
│       ├── forms.py           # 메모 폼
│       ├── urls.py            # 메모 URL
│       ├── admin.py           # 관리자 설정
│       └── tests.py           # 테스트
├── templates/                 # HTML 템플릿
│   ├── base.html              # 기본 템플릿
│   ├── home.html              # 홈페이지
│   ├── users/                 # 사용자 템플릿
│   │   ├── register.html
│   │   ├── login.html
│   │   └── profile.html
│   └── memos/                 # 메모 템플릿
│       ├── memo_list.html
│       ├── memo_detail.html
│       ├── memo_form.html
│       └── memo_confirm_delete.html
├── static/                    # 정적 파일 (CSS, JS)
│   ├── css/
│   └── js/
├── manage.py                  # Django 관리 명령어
├── requirements.txt           # 의존성 목록
└── README.md                  # 이 파일
```

## 🔒 보안 기능

- **CSRF 토큰**: 모든 폼에 적용되어 CSRF 공격 방지
- **SQL Injection 방지**: Django ORM 사용으로 안전한 데이터베이스 쿼리
- **XSS 방지**: 템플릿 자동 이스케이핑
- **패스워드 해싱**: Django 내장 알고리즘으로 안전한 비밀번호 저장
- **접근 제어**: 로그인 필수, 소유자만 메모 수정/삭제 가능

## 🧪 테스트 실행

### 전체 테스트 실행

```bash
python manage.py test
```

### 특정 앱 테스트

```bash
python manage.py test apps.users
python manage.py test apps.memos
```

### 상세 정보와 함께 테스트

```bash
python manage.py test -v 2
```

### 테스트 결과
- **총 테스트**: 7개
- **통과율**: 100% (7/7)

## 📦 의존성

```
Django==5.0.1 또는 1.7
python-dotenv==1.0.0
```

자세한 내용은 `requirements.txt`를 참고하세요.

## 🔧 설정 및 환경 변수

`.env` 파일에서 다음 설정을 할 수 있습니다:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_ENGINE=django.db.backends.sqlite3
DATABASE_NAME=db.sqlite3
```

## 📝 개발 가이드

### 코드 스타일
- Python: PEP 8 준수
- 함수/변수: 소문자 + 언더스코어
- 클래스: 파스칼 표기법
- 공백: 4칸 들여쓰기

### 테스트 작성
- Django TestCase 사용
- `test_` 접두어로 테스트 함수 명명
- setUp/tearDown으로 테스트 데이터 관리

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

## 👨‍💻 개발자

- GitHub: [@eunxxun](https://github.com/eunxxun)

## 🤝 기여

버그 리포트 및 기능 요청은 GitHub Issues에서 해주세요.

## 📞 지원

문제가 발생하면 GitHub Issues를 통해 문의해주세요.

---

**Happy Coding! 🚀**
