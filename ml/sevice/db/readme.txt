# bsgo 서비스를 통해 번역된 데이터를 저장하는 테이블
# 향후 적정량이 모이면 학습용으로 사용된다

CREATE TABLE `tbl_trans_lang_log` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`oCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '언어감지코드',
	`tCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '번역결과언어코드',
	`oStr` TEXT NULL DEFAULT NULL COMMENT '원문',
	`tStc` TEXT NULL DEFAULT NULL COMMENT '번역문',
	`regDate` TIMESTAMP NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB
;

#데이터 추가
INSERT INTO `py_db`.`tbl_trans_lang_log` 
(`oCode`, `tCode`, `oStr`, `tStc`, `regDate`) 
VALUES 
('en', 'ko', 'hello', '안녕', '2020-01-17 15:01:07');