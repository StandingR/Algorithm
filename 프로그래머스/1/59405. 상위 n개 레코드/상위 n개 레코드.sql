/*
■ 결과중 처음부터 1개만 가져오기

         mysql> SELECT * FROM [테이블명] LIMIT 1;

■ 결과중 100번째부터 10개만 가져오기. 첫번째 레코드는 0번 부터 시작한다.

         mysql> SELECT * FROM [테이블명] LIMIT 100, 10;

■ 조건절 줘서 검색결과 1개만 가져오기

     mysql > select [컬럼명] from [테이블명] where [조건절] limit 1;
ex) mysql > select mod from sysl where time='600' limit 1;


[출처] [Mysql]쿼리 결과중 첫번째 행만 가져오기, 특정 행만 가져오기|작성자 참좋은날
*/
SELECT NAME
FROM ANIMAL_INS 
ORDER BY DATETIME LIMIT 1;