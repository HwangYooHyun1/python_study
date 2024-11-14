USE market_db;

# A. 저장 테이블
DROP TABLE IF EXISTS price_index;
# 1. 테이블 전체 삭제
TRUNCATE TABLE price_index;

CREATE TABLE price_index (
    date VARCHAR(12),
    total_index FLOAT,
    food_non_alcoholic FLOAT,
    alcoholic_tobacco FLOAT,
    clothing_footwear FLOAT,
    housing_utilities_fuel FLOAT,
    household_goods_services FLOAT,
    health FLOAT,
    transport FLOAT,
    communication FLOAT,
    recreation_culture FLOAT,
    education FLOAT,
    food_hospitality FLOAT,
    other_goods_services FLOAT
);

SELECT * FROM price_index; 

DESC price_index; 

#######################################################################
-- date를 DATE 타입 변경을 위해 임의로 일자를 추가하여 완전한 형태의 일자로 변경 
UPDATE price_index 
SET date = STR_TO_DATE(CONCAT(date, '.01'), '%Y.%m.%d');
-- 데이터 타입 변경 
ALTER TABLE price_index MODIFY COLUMN date DATE; 

DESC price_index;

#######################################################################
-- 1994-2024 의류 및 신발 생활물가지수 비교
SELECT YEAR(date) AS year, total_index, clothing_footwear
FROM price_index
GROUP BY YEAR(date);

SELECT YEAR(date) AS year, total_index, clothing_footwear,
 food_hospitality, household_goods_services, health
FROM price_index
GROUP BY YEAR(date);

#######################################################################
-- 의류 및 신발 생활물가지수 추출 
SELECT DATE_FORMAT(date, '%Y-%m') AS yearMonth , clothing_footwear
FROM price_index 
WHERE YEAR(date) IN (1994,1995,1996,1997);

#######################################################################
-- 총지수보다 의류 및 신발의 지수가 낮은 연도별 월 정보 확인 
SELECT YEAR(date), COUNT(YEAR(date))  
FROM price_index
WHERE clothing_footwear > total_index
GROUP BY YEAR(date)
ORDER BY COUNT(YEAR(date)) DESC; 

#######################################################################
-- 물가상승률
DELIMITER $$
DROP PROCEDURE IF EXISTS inflationRate;
CREATE PROCEDURE inflationRate(Item VARCHAR(40))
BEGIN 
	SELECT year, 
    (sum_cf - LAG(sum_t) OVER (ORDER BY year)) / LAG(sum_t) OVER (ORDER BY year) * 100 AS t_growth_rate,
	(sum_item - LAG(sum_item) OVER (ORDER BY year)) / LAG(sum_item) OVER (ORDER BY year) * 100 AS i_growth_rate
	FROM (
    SELECT YEAR(date) AS year, SUM(total_index) as sum_t, SUM(Item) as sum_item 
	FROM price_index
	WHERE YEAR(date) != 2024)
    GROUP BY YEAR(date)) AS Y; 
END $$
DELIMITER ; 

CALL inflationFate('clothing_footwear');