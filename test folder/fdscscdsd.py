<!DOCTYPE html>
<html lang="ko">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="Content-Security-Policy: default-src 'self' *.ksa.hs.kr">
    <meta name="Cache-Control" content="no-store">
    <meta http-equiv="Cache-Control" content="no-cache"/>
    <meta http-equiv="Expires" content="0"/>
    <meta http-equiv="Pragma" content="no-cache"/>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>자가진단 - 한국과학영재학교</title>
    <link href="/Content/default?v=sYlkBuoc6Jd4frTZmkBgQBMZW4eRtvBPBgj0j0IeYnA1" rel="stylesheet"/>

    <script src="/bundles/modernizr?v=inCVuEFe6J4Q07A0AcRsbJic_UE5MwpRMNGcOtk94TE1"></script>

    
    

    <link href="/Content/jquery-confirm.min.css" rel="stylesheet" />
    <link href="/Content/app_custome.css" rel="stylesheet" />
    
</head>

<body>
<form action="/Home/Sub">
    <input type="hidden" id="MenuId" name="Menuid" value=""/>
    <input type="hidden" id="Cmd" name="Cmd" value=""/>
    <input type="hidden" id="DataId" name="DataId" value=""/>
</form>
<div id="wrap">

<ul class="skipnavi">
    <li>
        <a href="#header">상단 바로가기</a>
    </li>
    <li>
        <a href="#nav">메뉴 바로가기</a>
    </li>
    <li>
        <a href="#kcontent">내용 바로가기</a>
    </li>
    <li>
        <a href="#footer">하단 바로가기</a>
    </li>
</ul>
<!-- end jump-link -->
<div id="header" class="clearfix navbar-fixed-top">
    <div class="container">
        <div class="nav_open_btn visible-xs">
            <a href="#" title="메뉴열기">
                <i class="fa fa-bars"></i>
            </a>
        </div>
        <div class="search_open_btn visible-xs">
            <a href="#" title="검색창 열기">
                <i class="fa fa-search"></i><i class="fa fa-times"></i>
            </a>
        </div>
        <ul class="list-inline easy_use hidden-xs">
            <li>
                <a href="#" class="zoomIn">
                    <img src="/Content/images/zoomin-icon.png" alt="확대">
                </a>
            </li>
            <li>
                <a href="#" class="zoomInDown">
                    <img src="/Content/images/zoomout-icon.png" alt="축소">
                </a>
            </li>
            <li>
                <a href="#" class="zoomReset">
                    <img src="/Content/images/zoominit-icon.png" alt="기본">
                </a>
            </li>
            <li>
                <a href="#">
                    <img src="/Content/images/print-icon.png" alt="프린트">
                </a>
            </li>
            <li class="search-sm">
                <a href="#" class="search-open">
                    <img src="../../Content/images/search-icon.png" alt="검색">
                </a> <a href="#" class="search-close">
                    <img src="../../Content/images/close-icon.png" alt="닫기">
                </a>
            </li>
        </ul>
        <form class="top-search" method="GET" action="/Search/Index">
            <label class="sr-only" for="topsearchText">통합검색</label>
            <input name="searchText" type="text" id="topsearchText" />
            <a href="#" class="fa fa-search" title="검색" onclick="$(this).closest('form').submit();"></a>
        </form>

<form action="/Account/LogOff" class="navbar-right" id="logoutForm" method="post"><input name="__RequestVerificationToken" type="hidden" value="D4B1ikbEDucEj62eeCpS1sbSYO359XNTR6d-cHuZcwBV5gLkyPSTDa9aBLJ162oAPP8bxLE-K-8WtezApA_RMTG1uNElDN2wIV7mbSt99qVxlK0f4OJnB-qNDv-FhL0a6_Rk9N4ZaF2EJINGTpLAEA2" />    <ul class="list-inline top-link">
        <li>
            <a href="#" onclick="$(this).closest('form').submit(); return false;">로그아웃</a>
        </li>
        
        <li>
            <a href="https://www.ksa.hs.kr/Home/Sub/199">자가진단</a>
        </li>        
        <li>
            <a href="/Helper/SiteMap">사이트맵</a>
        </li>
                        <li>
            <a href="/Eng">ENG</a>
        </li>
    </ul>
</form>        <h1 class="logo">
            <a href="/">
                <img src="../../Content/images/logo.png" alt="한국과학영재학교">
            </a>
        </h1>
    </div>

    <!--// .container -->

</div><!-- end .header -->
<div id="gnb">
    <div class="container">
        <ul class="gnblist clearfix">
                <li class="main-menu1">
                        <a href="#">
                            <span class="glyphicon glyphicon-plus"></span> 학교정보
                        </a>

                    <ul class="submenu">
                                <li>
<a href="/Home/Sub/194">학교장 인사말</a>                                </li>
                                <li>
<a href="/Home/Sub/3">비전 및 교육목표</a>                                </li>
                                <li>
<a href="/Home/TeacherInfo/22">교직원소개</a>                                </li>
                                <li>
<a href="/Home/Sub/4">학교연혁</a>                                </li>
                                <li>
                                            <a href="/Home/Sub/11">학교의 상징물<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/133">학교의상징물</a>                                                </li>
                                                <li>
<a href="/Home/Board/186">KSA Video</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/12">학교현황<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/13">학교현황</a>                                                </li>
                                                <li>
<a href="/Home/Sub/14">건물배치도</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/15">장학<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/16">장학제도</a>                                                </li>
                                                <li>
<a href="/Home/Sub/18">장학금 수혜 현황</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/19">홍보자료<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Board/20">홍보사진</a>                                                </li>
                                                <li>
<a href="/Home/Board/21">동영상</a>                                                </li>
                                                <li>
<a href="/Home/Board/181">언론보도/ Media Report</a>                                                </li>
                                                <li>
<a href="/Home/Board/180">공개수업</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
<a href="/SchoolEvent/Index/135">학사일정</a>                                </li>
                                <li>
<a href="/Home/Sub/136">오시는길</a>                                </li>
                    </ul>

                </li>
                <li class="main-menu2">
                        <a href="#">
                            <span class="glyphicon glyphicon-plus"></span> 교육정보
                        </a>

                    <ul class="submenu">
                                <li>
                                            <a href="/Home/Sub/24">교육과정<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/130">운영방침</a>                                                </li>
                                                <li>
<a href="/Home/Sub/131">교육과정</a>                                                </li>
                                                <li>
<a href="/Home/Board/132">교육계획서</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
<a href="/Home/Sub/28">학부소개</a>                                </li>
                                <li>
                                            <a href="/Home/Sub/29">창의&#183;연구활동<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/30">창의&#183;연구활동</a>                                                </li>
                                                <li>
<a href="/Home/Sub/32">국외 위탁교육</a>                                                </li>
                                                <li>
<a href="/Home/Sub/31">국제공동연구</a>                                                </li>
                                                <li>
<a href="/Home/Sub/33">국제학술대회 및 국제과학영재 학술대회 참가</a>                                                </li>
                                                <li>
<a href="/Home/Sub/34">우수논문 국내&#183;외 발표</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/35">국제학술교류<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/37">자매결연학교 소개</a>                                                </li>
                                                <li>
<a href="/Home/Sub/36">교환학생 프로그램</a>                                                </li>
                                                <li>
<a href="/Home/Sub/38">교사교류 프로그램</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
<a href="/Home/Sub/39">역량중심 리더십활동</a>                                </li>
                                <li>
<a href="/Home/Sub/40">창의교육지원센터</a>                                </li>
                                <li>
                                            <a href="/Home/Sub/42">특별프로그램<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/43">KSASF</a>                                                </li>
                                                <li>
<a href="/Home/Sub/44">초청특강</a>                                                </li>
                                                <li>
<a href="/Home/Sub/45">KSA 과학영재교육 포럼</a>                                                </li>
                                                <li>
<a href="/Home/Sub/46">과학체험교실</a>                                                </li>
                                                <li>
<a href="/Home/Sub/47">과학영재학교 R&amp;E 및 우수연구 공동발표회</a>                                                </li>
                                                <li>
<a href="/Home/Sub/49">과학기술경영</a>                                                </li>
                                                <li>
<a href="/Home/Sub/50">창의공학</a>                                                </li>
                                            </ul>
                                </li>
                    </ul>

                </li>
                <li class="main-menu3">
                        <a href="http://admission.ksa.hs.kr" title="입학안내  사이트로 연결" target="_blank" class="link_icon">
                            <span class="glyphicon glyphicon-plus"></span> 입학안내<i class="fa fa-clone"></i>
                        </a>

                    <ul class="submenu">
                                <li>
                                                <a href="https://admission.ksa.hs.kr" target="_blank" data-id="104">입학안내</a>
                                </li>
                    </ul>

                </li>
                <li class="main-menu4">
                        <a href="#">
                            <span class="glyphicon glyphicon-plus"></span> 학교생활
                        </a>

                    <ul class="submenu">
                                <li>
<a href="/Home/Sub/51">도서관</a>                                </li>
                                <li>
                                                <a href="/Counsel" target="_blank" data-id="52">상담실</a>
                                </li>
                                <li>
                                            <a href="/Home/Sub/187">보건실<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/188">보건실</a>                                                </li>
                                                <li>
<a href="/Home/Board/189">게시판</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
<a href="/Home/Sub/56">생활관</a>                                </li>
                                <li>
<a href="/Home/Sub/57">학생성장센터</a>                                </li>
                                <li>
<a href="/Home/Application/58?class=menu_link">과학체험교실신청</a>                                </li>
                                <li>
<a href="/Home/Application/59?class=menu_link">학교견학신청</a>                                </li>
                                <li>
                                            <a href="/Home/Sub/60">백양관<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Board/61">백양관 게시판</a>                                                </li>
                                                <li>
<a href="/Home/BackYang/62">백양관 예약</a>                                                </li>
                                                <li>
<a href="/Home/BackYangQuery/63">백양관 예약내역</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/64">창조관<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/65">사용절차 및 이용안내</a>                                                </li>
                                                <li>
<a href="/Home/SearchMachine/66">기기검색</a>                                                </li>
                                                <li>
<a href="/Home/Booking/67">기기예약</a>                                                </li>
                                                <li>
<a href="/Home/BookList/68">예약현황 및 조회</a>                                                </li>
                                                <li>
<a href="/Home/Board/69">자료실</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/70">급식관리<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/CafeteriaMenu/72">식단표</a>                                                </li>
                                                <li>
<a href="/Home/Board/141">급식게시판</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
<a href="/Home/Board/142?class=menu_link">교재신청</a>                                </li>
                                <li>
                                            <a href="/Home/Sub/196">영수증 발급<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Bill/Index/197">영수증 발급</a>                                                </li>
                                                <li>
<a href="/Bill/CheckBill/198">영수증위변조확인</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/199">건강자가진단<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/SelfHealthCheck/Index/200">자가진단</a>                                                </li>
                                                <li>
<a href="/SelfHealthCheck/CheckHistory/201">자가진단목록</a>                                                </li>
                                            </ul>
                                </li>
                    </ul>

                </li>
                <li class="main-menu5">
                        <a href="#">
                            <span class="glyphicon glyphicon-plus"></span> 커뮤니티
                        </a>

                    <ul class="submenu">
                                <li>
<a href="/Home/Board/73?class=menu_link">재학생 게시판</a>                                </li>
                                <li>
<a href="/Home/Board/75?class=menu_link">학부모 게시판</a>                                </li>
                                <li>
<a href="/Home/Board/76?class=menu_link">졸업생 게시판</a>                                </li>
                    </ul>

                </li>
                <li class="main-menu6">
                        <a href="#">
                            <span class="glyphicon glyphicon-plus"></span> 정보서비스
                        </a>

                    <ul class="submenu">
                                <li>
                                            <a href="/Home/Sub/77">학교소식<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Board/78">공지사항</a>                                                </li>
                                                <li>
<a href="/Home/Board/79">언론보도/ Media Report</a>                                                </li>
                                                <li>
<a href="/Home/Board/80">학내소식</a>                                                </li>
                                                <li>
<a href="/Home/Board/137">영문공지사항</a>                                                </li>
                                                <li>
<a href="/Home/Board/139">주간일정</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/81">민원 서비스<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Suggest/82">건의함</a>                                                </li>
                                                <li>
<a href="/Home/Suggest/83">저작권 신고</a>                                                </li>
                                                <li>
<a href="/Home/Sub/84">개인정보처리방침</a>                                                </li>
                                                <li>
<a href="/Home/Sub/85">이메일집단수집거부</a>                                                </li>
                                            </ul>
                                </li>
                                <li>
<a href="/Home/Board/86?class=menu_link">학교 규정집</a>                                </li>
                                <li>
<a href="/Home/Board/105?class=menu_link">정보보호/정보윤리자료실</a>                                </li>
                                <li>
                                            <a href="/Home/Sub/106">정보공개방<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/108">정보공개제도안내</a>                                                </li>
                                                <li>
<a href="/Home/Sub/109">비공개세부기준</a>                                                </li>
                                                <li>
<a href="/Home/Board/111">정보목록공개</a>                                                </li>
                                                <li>
                                                                <a href="https://www.open.go.kr/" target="_blank">정보공개창구</a>
                                                </li>
                                            </ul>
                                </li>
                                <li>
                                            <a href="/Home/Sub/107">학교정보공시<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Sub/113">학교정보공시목록</a>                                                </li>
                                                <li>
<a href="/Home/Board/114">학교규칙 및 학교운영규정</a>                                                </li>
                                                <li>
<a href="/Home/Board/115">교육과정 편성 및 변동상황</a>                                                </li>
                                                <li>
<a href="/Home/Board/116">학생현황 및 변동상황</a>                                                </li>
                                                <li>
<a href="/Home/Board/182">학년별/교과별학습현황</a>                                                </li>
                                                <li>
<a href="/Home/Board/117">학교시설</a>                                                </li>
                                                <li>
<a href="/Home/Board/118">교원현황</a>                                                </li>
                                                <li>
<a href="/Home/Board/119">학교회계</a>                                                </li>
                                                <li>
<a href="/Home/Board/120">기관장업무추진비</a>                                                </li>
                                                <li>
<a href="/Home/Board/121">학교자문위원회</a>                                                </li>
                                                <li>
<a href="/Home/Board/122">학교급식</a>                                                </li>
                                                <li>
<a href="/Home/Board/123">보건/환경위생 및 안전관리</a>                                                </li>
                                                <li>
<a href="/Home/Board/124">학교폭력</a>                                                </li>
                                                <li>
<a href="/Home/Board/125">입학생 및 졸업생 현황</a>                                                </li>
                                                <li>
<a href="/Home/Board/127">고교프로파일</a>                                                </li>
                                                <li>
<a href="/Home/Board/183">우리학교 최고</a>                                                </li>
                                                <li>
<a href="/Home/Board/126">기 타</a>                                                </li>
                                            </ul>
                                </li>
                    </ul>

                </li>
                <li class="main-menu7">
                        <a href="#">
                            <span class="glyphicon glyphicon-plus"></span> 발전기금
                        </a>

                    <ul class="submenu">
                                <li>
<a href="/Home/Sub/93">인사말</a>                                </li>
                                <li>
<a href="/DevelopFund/Index/94">기금현황</a>                                </li>
                                <li>
<a href="/Home/Sub/95">기금용도</a>                                </li>
                                <li>
<a href="/DevelopFund/Donate/96">기금 참여하기</a>                                </li>
                                <li>
<a href="/Home/Sub/97">기부자 예우</a>                                </li>
                                <li>
<a href="/DevelopFund/MyPage/98">마이 페이지</a>                                </li>
                                <li>
                                            <a href="/Home/Sub/99">장학후원회<i class="fa fa-plus"></i><i class="fa fa-minus"></i></a>
                                            <ul class="submenu03">
                                                <li>
<a href="/Home/Board/100">장학금 후원방법</a>                                                </li>
                                                <li>
<a href="/Home/Board/102">역대장학후원회 현황</a>                                                </li>
                                                <li>
<a href="/Home/Board/103">Photo Gallery</a>                                                </li>
                                            </ul>
                                </li>
                    </ul>

                </li>
        </ul>
    </div>
</div>
<!--// nav -->
    <div class="sub-con">
        
<link rel="stylesheet" type="text/css" href="/Content/fonts.css">
<div class="container clearfix borderL">
<nav class="side_content hidden-xs">
    <h2 class="sub_title">
        학교생활 <span>Campus Life</span>
    </h2>
    <ul class="sub_gnb">
    <li>
<a class="" href="/Home/Sub/51">도서관</a>    </li>
    <li>
                <a href="/Counsel" target="_blank">상담실</a>
    </li>
                <li>
                        <a href="#" class="dropdown-collapse">
                            보건실<i class="fa fa-plus"></i><i class="fa fa-minus"></i>
                        </a>
                    <ul class="sub_gnb2">
                    <li>
<a class="" href="/Home/Sub/188">보건실</a>                    </li>
                    <li>
<a class="" href="/Home/Board/189">게시판</a>                    </li>
                    </ul>
                </li>
    <li>
    </li>
    <li>
<a class="" href="/Home/Sub/56">생활관</a>    </li>
    <li>
<a class="" href="/Home/Sub/57">학생성장센터</a>    </li>
    <li>
<a class="" href="/Home/Application/58">과학체험교실신청</a>    </li>
    <li>
<a class="" href="/Home/Application/59">학교견학신청</a>    </li>
                <li>
                        <a href="#" class="dropdown-collapse">
                            백양관<i class="fa fa-plus"></i><i class="fa fa-minus"></i>
                        </a>
                    <ul class="sub_gnb2">
                    <li>
<a class="" href="/Home/Board/61">백양관 게시판</a>                    </li>
                    <li>
<a class="" href="/Home/BackYang/62">백양관 예약</a>                    </li>
                    <li>
<a class="" href="/Home/BackYangQuery/63">백양관 예약내역</a>                    </li>
                    </ul>
                </li>
    <li>
    </li>
                <li>
                        <a href="#" class="dropdown-collapse">
                            창조관<i class="fa fa-plus"></i><i class="fa fa-minus"></i>
                        </a>
                    <ul class="sub_gnb2">
                    <li>
<a class="" href="/Home/Sub/65">사용절차 및 이용안내</a>                    </li>
                    <li>
<a class="" href="/Home/SearchMachine/66">기기검색</a>                    </li>
                    <li>
<a class="" href="/Home/Booking/67">기기예약</a>                    </li>
                    <li>
<a class="" href="/Home/BookList/68">예약현황 및 조회</a>                    </li>
                    <li>
<a class="" href="/Home/Board/69">자료실</a>                    </li>
                    </ul>
                </li>
    <li>
    </li>
                <li>
                        <a href="#" class="dropdown-collapse">
                            급식관리<i class="fa fa-plus"></i><i class="fa fa-minus"></i>
                        </a>
                    <ul class="sub_gnb2">
                    <li>
<a class="" href="/Home/CafeteriaMenu/72">식단표</a>                    </li>
                    <li>
<a class="" href="/Home/Board/141">급식게시판</a>                    </li>
                    </ul>
                </li>
    <li>
    </li>
    <li>
<a class="" href="/Home/Board/142">교재신청</a>    </li>
                <li>
                        <a href="#" class="dropdown-collapse">
                            영수증 발급<i class="fa fa-plus"></i><i class="fa fa-minus"></i>
                        </a>
                    <ul class="sub_gnb2">
                    <li>
<a class="" href="/Bill/Index/197">영수증 발급</a>                    </li>
                    </ul>
                </li>
    <li>
    </li>
                <li>
                        <a href="#" class="dropdown-collapse menu-container select">
                            건강자가진단<i class="fa fa-plus"></i><i class="fa fa-minus"></i>
                        </a>
                    <ul class="sub_gnb2">
                    <li>
<a class="select" href="/SelfHealthCheck/Index/200">자가진단</a>                    </li>
                    <li>
<a class="" href="/SelfHealthCheck/CheckHistory/201">자가진단목록</a>                    </li>
                    </ul>
                </li>
    <li>
    </li>
    </ul>
</nav>
    <!--//sub-nav-->
    <div class="sub_content clearfix" id="kcontent">
        <div class="page_top">
            <p class="page_location">
                <a href="/Eng" title="To Home">
                    <i class="fa fa-home"></i>
                </a><span><a href="/Home/Sub?menuId=7">학교생활</a></span>
                <span><a href="/Home/Sub?menuId=199">건강자가진단</a></span>
                <span>자가진단</span>
            </p>
            <h2 class="page_title">자가진단</h2>
            <span class="page_text hidden-xs">KSA! The Science-Gifted Institute Leading the Future</span>
        </div>
        <!-- .page_top end (상단 타이틀과 정보) -->
        <div class="page_content">
            

<link href="/Content/iCheck/square/_all.css" rel="stylesheet" />
<div id="selfcheck">
<form action="/SelfHealthCheck/Update" enctype="multipart/form-data" id="SelfHealthCheckForm" method="post"><input name="__RequestVerificationToken" type="hidden" value="KRId3ngNJXf9UZi_KFgU_eOZYle6bouwMbcMVnnaSRf5OYxVWDRqBq1iX_Vf6spRXDqXTrtIFjv7VILv2XrJAmcrf9FNv0kpU3cmHKHK-XyWAlmd5LqCuzAZ--vd1cs8h2ZrBluvjIw4uFQN0ZPzew2" /><input data-val="true" data-val-number="CheckId 필드는 숫자여야 합니다." data-val-required="CheckId 필드가 필요합니다." id="CheckId" name="CheckId" type="hidden" value="5158" /><input data-val="true" data-val-number="CheckItemId 필드는 숫자여야 합니다." data-val-required="CheckItemId 필드가 필요합니다." id="SelfCheckItemDatas_0__CheckItemId" name="SelfCheckItemDatas[0].CheckItemId" type="hidden" value="15478" /><input data-val="true" data-val-number="CheckItemId 필드는 숫자여야 합니다." data-val-required="CheckItemId 필드가 필요합니다." id="SelfCheckItemDatas_1__CheckItemId" name="SelfCheckItemDatas[1].CheckItemId" type="hidden" value="15479" /><input data-val="true" data-val-number="CheckItemId 필드는 숫자여야 합니다." data-val-required="CheckItemId 필드가 필요합니다." id="SelfCheckItemDatas_2__CheckItemId" name="SelfCheckItemDatas[2].CheckItemId" type="hidden" value="15480" /><input data-val="true" data-val-number="Order 필드는 숫자여야 합니다." data-val-required="Order 필드가 필요합니다." id="SelfCheckItemDatas_0__Order" name="SelfCheckItemDatas[0].Order" type="hidden" value="1" /><input data-val="true" data-val-number="Order 필드는 숫자여야 합니다." data-val-required="Order 필드가 필요합니다." id="SelfCheckItemDatas_1__Order" name="SelfCheckItemDatas[1].Order" type="hidden" value="2" /><input data-val="true" data-val-number="Order 필드는 숫자여야 합니다." data-val-required="Order 필드가 필요합니다." id="SelfCheckItemDatas_2__Order" name="SelfCheckItemDatas[2].Order" type="hidden" value="3" />        <div class="guide">
            <ul class="info">
                <li> 이 설문지는 코로나-19 감염예방을 위하여 교직원 및 학생의 건강 상태를 확인하는 내용입니다. </li>
                <li> 설문에 성실하게 응답하여 주시기 바랍니다. </li>
            </ul>
        </div>
        <div class="selfcheck_question" id="health_check">
            <dl>
                <dt>
                    1. 몸에 <span>열</span>이 있나요?
                    (해당사항 선택)
                    <br>단, 기저질환 등으로 코로나19와 관계없이 평소에 발열 증상이 계속되는 경우는 제외
                </dt>
                <dd>
                    <div class="answer_item">
                        <input Name="survey_q1" checked="checked" class="survey_q1 suvery_answ" data-target="q1a1" data-value="0" id="survey_q1a1" name="SelfCheckItemDatas[0].CheckValue" type="radio" value="False" />

                        <input data-val="true" data-val-number="Int32 필드는 숫자여야 합니다." data-val-required="Int32 필드가 필요합니다." id="q1a1" name="SelfCheckItemDatas[0].CheckResultValues[0]" type="hidden" value="0" />
                        <label for="survey_q1a1">37.5℃ 미만</label>
                    </div>
                    <div class="answer_item">
                        <input Name="survey_q1" class="survey_q1  suvery_answ" data-target="q1a1" data-value="1" id="survey_q1a2" name="SelfCheckItemDatas[0].CheckValue" type="radio" value="True" />
                        <label for="survey_q1a2">37.5℃ 이상 및 발열감</label>
                    </div>
                </dd>
            </dl>
            <dl>
                <dt>
                    2. 감염이 의심되는 <span>증상</span>이 있나요? 
                    <br>* 기침, 인후통, 호흡곤란, 오한, 근육통, 두통, 후각·미각 소실 또는 폐렴. 단, 기저질환 등으로 코로나19와 관계없이 평소에 위의 증상이 계속되는 경우는 제외
                </dt>
                <dd>
                    <div class="answer_item">
                        <input Name="survey_q2" checked="checked" class="survey_q2  suvery_answ" data-target="q2a1" data-value="0" id="survey_q2a1" name="SelfCheckItemDatas[1].CheckValue" type="radio" value="False" />
                        <input data-val="true" data-val-number="Int32 필드는 숫자여야 합니다." data-val-required="Int32 필드가 필요합니다." id="q2a1" name="SelfCheckItemDatas[1].CheckResultValues[0]" type="hidden" value="0" />
                        <label for="survey_q2a1">아니오</label>
                    </div>
                    <div class="answer_item">
                        <input Name="survey_q2" class="survey_q2  suvery_answ" data-target="q2a1" data-value="1" id="survey_q2a2" name="SelfCheckItemDatas[1].CheckValue" type="radio" value="True" />
                        <label for="survey_q2a2">예</label>
                    </div>
                </dd>
            </dl>
            <dl>
                <dt>
                    3.<span> 본인 또는 동거인</span>이 방역당국에 의해 현재 <span>자가격리</span>가 이루어지고 있나요?
                    <br>* <방역당국 지침> 최근 14일 이내 해외 입국자, 확진자와 접촉자 등은 자가격리 조치. 단, 직업특성상 잦은 해외 입·출국으로 의심증상이 없는 경우는 자가격리 면제
                </dt>
                <dd>
                    <div class="answer_item">
                        <input Name="survey_q3" checked="checked" class="survey_q3  suvery_answ" data-target="q3a1" data-value="0" id="survey_q3a1" name="SelfCheckItemDatas[2].CheckValue" type="radio" value="False" />
                        <input data-val="true" data-val-number="Int32 필드는 숫자여야 합니다." data-val-required="Int32 필드가 필요합니다." id="q3a1" name="SelfCheckItemDatas[2].CheckResultValues[0]" type="hidden" value="0" />
                        <label for="survey_q3a1">아니오</label>
                    </div>
                    <div class="answer_item">
                        <input Name="survey_q3" class="survey_q3  suvery_answ" data-target="q3a1" data-value="1" id="survey_q3a2" name="SelfCheckItemDatas[2].CheckValue" type="radio" value="True" />
                        <label for="survey_q3a2">예</label>
                    </div>
                </dd>
            </dl>
            <input type="submit" id="btnConfirm" class="btn btn-primary" style="width:100%;" value="제출 / Submit" />
        </div>
</form></div>


        </div>
    </div>
</div>

    </div>
    <div id="footer">
        <div class="f_list_link">
            <div class="container">
                <ul>
                    <li>
                        <a href="/Home/Sub/84">개인정보처리방침</a>
                    </li>
                    <li>
                        <a href="/Home/Sub/85">이메일무단수집거부</a>
                    </li>
                    <!--li><a href="../Userguide/terms_use.html">이용약관</a></li-->
                    <li>
                        <a href="/Home/Sub/136">오시는길</a>
                    </li>
                    <li>&nbsp;</li>

                </ul>
            </div>
        </div>
        <div class="container">
            <!-- 관련사이트 모음 (링크 바로연결) -->
            <div class="family_site">
                <a href="#">Family Site<i class="fa fa-caret-up"></i></a>
<ul class="family_site_open">
        <li><a href="https://keis.ksa.hs.kr/" target="_blank" rel="noopener noreferrer">교직원웹</a></li>
        <li><a href="https://students.ksa.hs.kr/" target="_blank" rel="noopener noreferrer">학생웹</a></li>
        <li><a href="https://parents.ksa.hs.kr/" target="_blank" rel="noopener noreferrer">학부모웹</a></li>
        <li><a href="http://lms.ksa.hs.kr/" target="_blank" rel="noopener noreferrer">LMS</a></li>
        <li><a href="http://cc.ksa.hs.kr/" target="_blank" rel="noopener noreferrer">ECC</a></li>
        <li><a href="http://library.ksa.hs.kr/" target="_blank" rel="noopener noreferrer">도서관</a></li>
        <li><a href="https://gaonnuri.ksain.net/xe/?mid=login" target="_blank" rel="noopener noreferrer">학생회</a></li>
        <li><a href="/Home/Board/142" target="_blank" rel="noopener noreferrer">교재신청</a></li>
        <li><a href="https://admission.ksa.hs.kr/iphak_eng/" target="_blank" rel="noopener noreferrer">Admissions</a></li>
        <li><a href="http://www.schoolhealth.kr/" target="_blank" rel="noopener noreferrer">학생건강정보센터</a></li>
        <li><a href="http://rne.ksa.hs.kr/" target="_blank" rel="noopener noreferrer">KSA-Research Activities</a></li>
</ul>

            </div>
            <p class="f_number">
                대표전화 : 051-897-0006<span>|</span>FAX : 051-894-0280<span>|</span><a href="mailto:master@ksa.hs.kr">메일문의</a>
            </p>
            <address>
                47162 부산광역시 부산진구 백양관문로 105-47(당감동, 한국과학영재학교)
            </address>
            <p class="f_warning"> 저작물의 무단 전재 및 배포 시 저작권법 136조에 의거 최고 5년 이하의 징역 또는 5천만원 이하의 벌금에 처하거나 이를 병과할 수 있습니다. </p>
            <p class="copy">Copyright (c) 2015 KOREA SCIENCE ACADEMY. ALL RIGHTS RESERVED.</p>
        </div>
    </div>
    <!--//#footer-->
    <div id="slide_quick">
        <a href="#" class="slide_quick_btn">빠른메뉴</a>
        <div class="slide_area">
            <ul>
<!-- 
                <li>
                    <a href="http://sas.ksa.hs.kr/" target="_blank"><img src="~/Content/images/quick_icon-9.png" alt="교직원웹 포털">&nbsp;교직원웹</a>
                </li>
 -->
                <li>
                    <a href="http://students.ksa.hs.kr/" target="_blank" rel="noopener noreferrer"><img src="/Content/images/quick_icon-10.png" alt="학생웹 포털">&nbsp;학생웹</a>
                </li>
                <li>
                    <a href="http://parents.ksa.hs.kr/" target="_blank" rel="noopener noreferrer"><img src="/Content/images/quick_icon-11.png" alt="학부모웹 포털">&nbsp;학부모웹</a>
                </li>
                <li>
                    <a href="/Home/Sub/2"><img src="/Content/images/quick_icon-1.png" alt="학교장 인사말">&nbsp;학교장 인사말</a>
                </li>
                <li>
                    <a href="/Home/Sub/3"><img src="/Content/images/quick_icon-2.png" alt="교육목표">&nbsp;교육목표</a>
                </li>
                <li>
                    <a href="/Home/Sub/4"><img src="/Content/images/quick_icon-3.png" alt="학교연혁">&nbsp;학교연혁</a>
                </li>
                <li>
                    <a href="/Home/Sub/16"><img src="/Content/images/quick_icon-4.png" alt="장학제도">&nbsp;장학제도</a>
                </li>
                <li>
                    <a href="/Home/Sub/107"><img src="/Content/images/quick_icon-5.png" alt="학교 알리미">&nbsp;학교 알리미</a>
                </li>
                <li>
                    <a href="/Home/Sub/28"><img src="/Content/images/quick_icon-6.png" alt="학부소개">&nbsp;학부소개</a>
                </li>
                <li>
                    <a href="/Home/Suggest/82"><img src="/Content/images/quick_icon-7.png" alt="민원 서비스">&nbsp;민원 서비스</a>
                </li>
                <li>
                    <a href="/Home/Sub/136"><img src="/Content/images/quick_icon-8.png" alt="오시는 길">&nbsp;오시는 길</a>
                </li>
            </ul>
<!--
            <div class="counsel_number">
                <p>
                    <img src="~/Content/images/quick_icon-tel.png" alt="입학상담문의"> &nbsp;입학상담문의
                </p>
                <p class="call_number">051-606-2265</p>
                <p class="call_number">051-606-2273</p>
                <p class="call_number">051-606-2182</p>
            </div>
-->
        </div>
    </div>
    <!-- #quick_btn end -->
    <a href="#wrap" class="top_btn">상단으로</a>

</div>
<script src="/bundles/jquery?v=MUwaZlQJn5GzAHWcIdCtxyien7uWD535ET23r4alxFA1"></script>

<script src="/bundles/bootstrap?v=OfX192nbUgK5NE8ftV4Ef6ToCtjUTli3wC5jn344bfM1"></script>

<script src="/bundles/jqueryui?v=nmuMA-O4C0zphhL2ApoyudBi4v4VCXr0cCFlFmBK2eU1"></script>

   
<script src="/Scripts/ksa.js"></script>
<script src="/Scripts/jquery.jcarousellite.min.js"></script>
<script src="/Scripts/jquery-confirm.min.js"></script>
    
    
    <script src="/Scripts/app/selfcheck.min.js"></script>

    <script src="/Scripts/jquery.icheck.min.js"></script>
    

    <script src="/Scripts/app/sub.js"></script>
</body>
</html>
