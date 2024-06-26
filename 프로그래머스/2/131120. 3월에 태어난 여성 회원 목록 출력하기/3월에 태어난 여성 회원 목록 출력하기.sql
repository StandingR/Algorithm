/*
1. MEMBER_PROFILE 테이블에서 
2. 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 
3. 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 
4.결과는 회원ID를 기준으로 오름차순 정렬해주세요.

*/


SELECT MEMBER_ID,MEMBER_NAME,GENDER,
DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
FROM MEMBER_PROFILE
where GENDER = "W" and DATE_OF_BIRTH like "%03%"
and not TLNO like "%NULL%"
order by MEMBER_ID;