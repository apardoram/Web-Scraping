from RobotScraper import RobotScraper

rs = RobotScraper("https://espndeportes.espn.com/basquetbol/nba/duelo?juegoId=401359859")
rs.init_extract()
# print(rs.get_df())
rs.save_df()
