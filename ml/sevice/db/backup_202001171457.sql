-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.4.11-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- py_db 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `py_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `py_db`;

-- 테이블 py_db.tbl_trans_lang_log 구조 내보내기
CREATE TABLE IF NOT EXISTS `tbl_trans_lang_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `oCode` varchar(4) DEFAULT NULL COMMENT '언어감지코드',
  `tCode` varchar(4) DEFAULT NULL COMMENT '번역결과언어코드',
  `oStr` text DEFAULT NULL COMMENT '원문',
  `tStc` text DEFAULT NULL COMMENT '번역문',
  `regDate` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='bsgo 사이트를 사용한 번역 로그 테이블\r\n해당 데이터는 어느정도 쌓이면 학습용 데이터로 사용된다';

-- 테이블 데이터 py_db.tbl_trans_lang_log:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `tbl_trans_lang_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `tbl_trans_lang_log` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
