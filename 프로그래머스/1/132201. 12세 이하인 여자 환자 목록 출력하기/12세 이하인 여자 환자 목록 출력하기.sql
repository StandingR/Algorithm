/*
1.PATIENT 테이블에서 
2. 12세 이하인 여자환자의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회하는 SQL문을 작성해주세요. 
3.이때 전화번호가 없는 경우, 'NONE'으로 출력시켜 주시고 
 = IFNULL(column_name, replacement_value)
4.결과는 나이를 기준으로 내림차순 정렬하고,
5.나이 같다면 환자이름을 기준으로 오름차순 정렬해주세요.
SELECT *
FROM   주문테이블
ORDER BY (CASE WHEN 주문상태 = '배송완료' THEN 1 ELSE 2 END), 주문일자 ASC;
*/
SELECT PT_NAME, PT_NO, GEND_CD, AGE,IFNULL(TLNO, 'NONE')as TLNO
FROM PATIENT
WHERE GEND_CD like "%W%" and AGE <= 12
order BY AGE DESC, PT_NAME;