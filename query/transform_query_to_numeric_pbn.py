# Deklarasi jumlah node untuk setiap label (entitas Film/Movie)
movie_node_counts = {
    "action": 293467,
    "adult": 222819,
    "adventure": 273401,
    "animation": 330135,
    "biography": 76749,
    "comedy": 1479294,
    "crime": 312629,
    "documentary": 618520,
    "drama": 1984332,
    "family": 489281,
    "fantasy": 155302,
    "film_noir": 784,
    "game_show": 225632,
    "history": 95891,
    "horror": 130261,
    "music": 356267,
    "musical": 54325,
    "mystery": 149470,
    "news": 408975,
    "reality_tv": 338752,
    "romance": 644609,
    "sci_fi": 89121,
    "sport": 137057,
    "talk_show": 773293,
    "thriller": 124666,
    "war": 26911,
    "western": 26970
}

# Deklarasi jumlah node untuk setiap label (entitas Person)
person_node_counts = {
    "actor": 1263984,
    "actress": 767812,
    "animation_department": 27980,
    "art_department": 62619,
    "art_director": 27370,
    "assistant": 443,
    "assistant_director": 84613,
    "camera_department": 186421,
    "casting_department": 13843,
    "casting_director": 10628,
    "cinematographer": 284302,
    "composer": 248066,
    "costume_department": 14904,
    "costume_designer": 11048,
    "director": 560717,
    "editor": 257000,
    "editorial_department": 63380,
    "electrical_department": 2,
    "executive": 9007,
    "legal": 437,
    "location_management": 13050,
    "make_up_department": 18686,
    "manager": 3122,
    "miscellaneous": 228889,
    "music_department": 76607,
    "producer": 613186,
    "production_department": 1,
    "production_designer": 51274,
    "production_manager": 51119,
    "publicist": 581,
    "script_department": 21987,
    "set_decorator": 9893,
    "sound_department": 80900,
    "soundtrack": 99799,
    "special_effects": 11232,
    "stunts": 21182,
    "talent_agent": 2291,
    "transportation_department": 4459,
    "visual_effects": 36300,
    "writer": 683795
}

# Deklarasi jumlah node untuk label/entitas Category hasil refactoring
category_label_counts = {
    "tvEpisode": 1,
    "short": 1,
    "movie": 1,
    "video": 1,
    "tvSeries": 1,
    "tvMovie": 1,
    "tvMiniSeries": 1,
    "tvSpecial": 1,
    "videoGame": 1,
    "tvShort": 1,
    "audiobook": 1,
    "radioSeries": 1,
    "episode": 1
}

# Deklarasi jumlah node untuk label/entitas Year hasil refactoring
year_label_counts = {
    "year_2115": 1, "year_2028": 1, "year_2027": 1, "year_2026": 1, "year_2025": 1, 
    "year_2024": 1, "year_2023": 1, "year_2022": 1, "year_2021": 1, "year_2020": 1, 
    "year_2019": 1, "year_2018": 1, "year_2017": 1, "year_2016": 1, "year_2015": 1, 
    "year_2014": 1, "year_2013": 1, "year_2012": 1, "year_2011": 1, "year_2010": 1, 
    "year_2009": 1, "year_2008": 1, "year_2007": 1, "year_2006": 1, "year_2005": 1, 
    "year_2004": 1, "year_2003": 1, "year_2002": 1, "year_2001": 1, "year_2000": 1, 
    "year_1999": 1, "year_1998": 1, "year_1997": 1, "year_1996": 1, "year_1995": 1, 
    "year_1994": 1, "year_1993": 1, "year_1992": 1, "year_1991": 1, "year_1990": 1, 
    "year_1989": 1, "year_1988": 1, "year_1987": 1, "year_1986": 1, "year_1985": 1, 
    "year_1984": 1, "year_1983": 1, "year_1982": 1, "year_1981": 1, "year_1980": 1, 
    "year_1979": 1, "year_1978": 1, "year_1977": 1, "year_1976": 1, "year_1975": 1, 
    "year_1974": 1, "year_1973": 1, "year_1972": 1, "year_1971": 1, "year_1970": 1, 
    "year_1969": 1, "year_1968": 1, "year_1967": 1, "year_1966": 1, "year_1965": 1, 
    "year_1964": 1, "year_1963": 1, "year_1962": 1, "year_1961": 1, "year_1960": 1, 
    "year_1959": 1, "year_1958": 1, "year_1957": 1, "year_1956": 1, "year_1955": 1, 
    "year_1954": 1, "year_1953": 1, "year_1952": 1, "year_1951": 1, "year_1950": 1, 
    "year_1949": 1, "year_1948": 1, "year_1947": 1, "year_1946": 1, "year_1945": 1, 
    "year_1944": 1, "year_1943": 1, "year_1942": 1, "year_1941": 1, "year_1940": 1, 
    "year_1939": 1, "year_1938": 1, "year_1937": 1, "year_1936": 1, "year_1935": 1, 
    "year_1934": 1, "year_1933": 1, "year_1932": 1, "year_1931": 1, "year_1930": 1, 
    "year_1929": 1, "year_1928": 1, "year_1927": 1, "year_1926": 1, "year_1925": 1, 
    "year_1924": 1, "year_1923": 1, "year_1922": 1, "year_1921": 1, "year_1920": 1, 
    "year_1919": 1, "year_1918": 1, "year_1917": 1, "year_1916": 1, "year_1915": 1, 
    "year_1914": 1, "year_1913": 1, "year_1912": 1, "year_1911": 1, "year_1910": 1, 
    "year_1909": 1, "year_1908": 1, "year_1907": 1, "year_1906": 1, "year_1905": 1, 
    "year_1904": 1, "year_1903": 1, "year_1902": 1, "year_1901": 1, "year_1900": 1, 
    "year_1899": 1, "year_1898": 1, "year_1897": 1, "year_1896": 1, "year_1895": 1, 
    "year_1894": 1, "year_1893": 1, "year_1892": 1, "year_1891": 1, "year_1890": 1, 
    "year_1889": 1, "year_1888": 1, "year_1887": 1, "year_1886": 1, "year_1885": 1, 
    "year_1884": 1, "year_1883": 1, "year_1882": 1, "year_1881": 1, "year_1880": 1, 
    "year_1879": 1, "year_1878": 1, "year_1877": 1, "year_1876": 1, "year_1875": 1, 
    "year_1874": 1, "year_1873": 1, "year_1872": 1, "year_1871": 1, "year_1870": 1, 
    "year_1869": 1, "year_1868": 1, "year_1867": 1, "year_1866": 1, "year_1865": 1, 
    "year_1864": 1, "year_1863": 1, "year_1862": 1, "year_1861": 1, "year_1860": 1, 
    "year_1859": 1, "year_1858": 1, "year_1857": 1, "year_1856": 1, "year_1855": 1, 
    "year_1854": 1, "year_1853": 1, "year_1852": 1, "year_1851": 1, "year_1850": 1, 
    "year_1849": 1, "year_1848": 1, "year_1847": 1, "year_1846": 1, "year_1845": 1, 
    "year_1844": 1, "year_1843": 1, "year_1842": 1, "year_1841": 1, "year_1840": 1, 
    "year_1839": 1, "year_1838": 1, "year_1837": 1, "year_1836": 1, "year_1835": 1, 
    "year_1834": 1, "year_1833": 1, "year_1832": 1, "year_1831": 1, "year_1830": 1, 
    "year_1829": 1, "year_1828": 1, "year_1827": 1, "year_1826": 1, "year_1825": 1, 
    "year_1824": 1, "year_1823": 1, "year_1822": 1, "year_1821": 1, "year_1820": 1, 
    "year_1819": 1, "year_1818": 1, "year_1817": 1, "year_1816": 1, "year_1815": 1, 
    "year_1814": 1, "year_1813": 1, "year_1812": 1, "year_1811": 1, "year_1810": 1, 
    "year_1809": 1, "year_1808": 1, "year_1807": 1, "year_1806": 1, "year_1805": 1, 
    "year_1804": 1, "year_1803": 1, "year_1802": 1, "year_1801": 1, "year_1800": 1, 
    "year_1799": 1, "year_1798": 1, "year_1797": 1, "year_1796": 1, "year_1795": 1, 
    "year_1794": 1, "year_1793": 1, "year_1792": 1, "year_1791": 1, "year_1790": 1, 
    "year_1789": 1, "year_1788": 1, "year_1787": 1, "year_1786": 1, "year_1785": 1, 
    "year_1784": 1, "year_1783": 1, "year_1782": 1, "year_1781": 1, "year_1780": 1, 
    "year_1779": 1, "year_1778": 1, "year_1777": 1, "year_1776": 1, "year_1775": 1, 
    "year_1774": 1, "year_1773": 1, "year_1772": 1, "year_1771": 1, "year_1770": 1, 
    "year_1769": 1, "year_1768": 1, "year_1767": 1, "year_1766": 1, "year_1765": 1, 
    "year_1764": 1, "year_1763": 1, "year_1761": 1, "year_1760": 1, "year_1759": 1, 
    "year_1758": 1, "year_1757": 1, "year_1756": 1, "year_1755": 1, "year_1754": 1, 
    "year_1751": 1, "year_1750": 1, "year_1749": 1, "year_1748": 1, "year_1747": 1, 
    "year_1746": 1, "year_1745": 1, "year_1744": 1, "year_1743": 1, "year_1741": 1, 
    "year_1740": 1, "year_1739": 1, "year_1737": 1, "year_1736": 1, "year_1735": 1, 
    "year_1734": 1, "year_1733": 1, "year_1732": 1, "year_1731": 1, "year_1730": 1, 
    "year_1729": 1, "year_1728": 1, "year_1727": 1, "year_1726": 1, "year_1725": 1, 
    "year_1724": 1, "year_1723": 1, "year_1722": 1, "year_1720": 1, "year_1718": 1, 
    "year_1717": 1, "year_1716": 1, "year_1715": 1, "year_1714": 1, "year_1713": 1, 
    "year_1712": 1, "year_1711": 1, "year_1710": 1, "year_1707": 1, "year_1706": 1, 
    "year_1703": 1, "year_1701": 1, "year_1700": 1, "year_1699": 1, "year_1698": 1, 
    "year_1697": 1, "year_1696": 1, "year_1695": 1, "year_1694": 1, "year_1693": 1, 
    "year_1689": 1, "year_1688": 1, "year_1686": 1, "year_1685": 1, "year_1684": 1, 
    "year_1681": 1, "year_1679": 1, "year_1678": 1, "year_1677": 1, "year_1676": 1, 
    "year_1674": 1, "year_1673": 1, "year_1672": 1, "year_1671": 1, "year_1670": 1, 
    "year_1669": 1, "year_1668": 1, "year_1667": 1, "year_1664": 1, "year_1660": 1, 
    "year_1659": 1, "year_1658": 1, "year_1657": 1, "year_1656": 1, "year_1655": 1, 
    "year_1654": 1, "year_1653": 1, "year_1652": 1, "year_1651": 1, "year_1648": 1, 
    "year_1646": 1, "year_1645": 1, "year_1644": 1, "year_1643": 1, "year_1641": 1, 
    "year_1640": 1, "year_1639": 1, "year_1638": 1, "year_1637": 1, "year_1636": 1, 
    "year_1635": 1, "year_1634": 1, "year_1633": 1, "year_1632": 1, "year_1631": 1, 
    "year_1630": 1, "year_1629": 1, "year_1628": 1, "year_1627": 1, "year_1626": 1, 
    "year_1625": 1, "year_1623": 1, "year_1622": 1, "year_1621": 1, "year_1619": 1, 
    "year_1618": 1, "year_1616": 1, "year_1614": 1, "year_1613": 1, "year_1611": 1, 
    "year_1610": 1, "year_1609": 1, "year_1608": 1, "year_1606": 1, "year_1604": 1, 
    "year_1602": 1, "year_1601": 1, "year_1600": 1, "year_1599": 1, "year_1595": 1, 
    "year_1594": 1, "year_1593": 1, "year_1592": 1, "year_1591": 1, "year_1589": 1, 
    "year_1587": 1, "year_1586": 1, "year_1585": 1, "year_1584": 1, "year_1583": 1, 
    "year_1581": 1, "year_1580": 1, "year_1579": 1, "year_1578": 1, "year_1577": 1, 
    "year_1576": 1, "year_1574": 1, "year_1572": 1, "year_1571": 1, "year_1569": 1, 
    "year_1568": 1, "year_1567": 1, "year_1566": 1, "year_1564": 1, "year_1563": 1, 
    "year_1562": 1, "year_1561": 1, "year_1560": 1, "year_1558": 1, "year_1556": 1, 
    "year_1553": 1, "year_1550": 1, "year_1549": 1, "year_1547": 1, "year_1544": 1, 
    "year_1543": 1, "year_1542": 1, "year_1541": 1, "year_1540": 1, "year_1533": 1, 
    "year_1532": 1, "year_1530": 1, "year_1529": 1, "year_1527": 1, "year_1525": 1, 
    "year_1524": 1, "year_1521": 1, "year_1519": 1, "year_1511": 1, "year_1510": 1, 
    "year_1508": 1, "year_1506": 1, "year_1505": 1, "year_1504": 1, "year_1503": 1, 
    "year_1494": 1, "year_1493": 1, "year_1492": 1, "year_1485": 1, "year_1479": 1, 
    "year_1475": 1, "year_1474": 1, "year_1473": 1, "year_1471": 1, "year_1470": 1, 
    "year_1469": 1, "year_1468": 1, "year_1465": 1, "year_1463": 1, "year_1452": 1, 
    "year_1448": 1, "year_1440": 1, "year_1431": 1, "year_1422": 1, "year_1420": 1, 
    "year_1414": 1, "year_1413": 1, "year_1412": 1, "year_1408": 1, "year_1400": 1, 
    "year_1398": 1, "year_1375": 1, "year_1361": 1, "year_1350": 1, "year_1343": 1, 
    "year_1335": 1, "year_1330": 1, "year_1321": 1, "year_1313": 1, "year_1291": 1, 
    "year_1283": 1, "year_1273": 1, "year_1265": 1, "year_1250": 1, "year_1220": 1, 
    "year_1207": 1, "year_1191": 1, "year_1180": 1, "year_1179": 1, "year_1155": 1, 
    "year_1150": 1, "year_1130": 1, "year_1098": 1, "year_1095": 1, "year_1067": 1, 
    "year_1031": 1, "year_973": 1, "year_840": 1, "year_770": 1, "year_485": 1, 
    "year_235": 1, "year_165": 1, "year_163": 1, "year_140": 1, "year_122": 1, 
    "year_95": 1, "year_69": 1, "year_66": 1, "year_65": 1, "year_59": 1, 
    "year_46": 1, "year_37": 1, "year_27": 1, "year_21": 1, "year_17": 1, 
    "year_6": 1, "year_5": 1, "year_4": 1, "year_0": 1
}

# Deklarasi jumlah relasi KELUAR (Outgoing) dari entitas Person (Updated dengan BORN_IN & DIED_IN)
outgoing_rel_counts = {
    "actor": {
        "ACTED_IN": 11460681, "ARCHIVE_FOOTAGE_MAKER_OF": 88930, "ARCHIVE_SOUND_MAKER_OF": 1605, 
        "CINEMATOGRAPHER_OF": 112385, "COMPOSED": 168155, "DIRECTED": 749294, "EDITED": 72098, 
        "PRODUCED": 274473, "PRODUCTION_DESIGNER_OF": 13833, "WROTE": 878695,
        "BORN_IN": 1263984, "DIED_IN": 1263984
    },
    "actress": {
        "ACTED_IN": 8169427, "ARCHIVE_FOOTAGE_MAKER_OF": 60446, "ARCHIVE_SOUND_MAKER_OF": 360, 
        "CINEMATOGRAPHER_OF": 7394, "COMPOSED": 11426, "DIRECTED": 100076, "EDITED": 17236, 
        "PRODUCED": 109240, "PRODUCTION_DESIGNER_OF": 6100, "WROTE": 269132,
        "BORN_IN": 767812, "DIED_IN": 767812
    },
    "animation_department": {
        "ACTED_IN": 42345, "ARCHIVE_FOOTAGE_MAKER_OF": 344, "ARCHIVE_SOUND_MAKER_OF": 39, 
        "CINEMATOGRAPHER_OF": 6233, "COMPOSED": 3068, "DIRECTED": 147668, "EDITED": 12685, 
        "PRODUCED": 18025, "PRODUCTION_DESIGNER_OF": 3705, "WROTE": 52885,
        "BORN_IN": 27980, "DIED_IN": 27980
    },
    "art_department": {
        "ACTED_IN": 122054, "ARCHIVE_FOOTAGE_MAKER_OF": 1191, "ARCHIVE_SOUND_MAKER_OF": 32, 
        "CINEMATOGRAPHER_OF": 11407, "COMPOSED": 5877, "DIRECTED": 142373, "EDITED": 18001, 
        "PRODUCED": 30184, "PRODUCTION_DESIGNER_OF": 156063, "WROTE": 63679,
        "BORN_IN": 62619, "DIED_IN": 62619
    },
    "art_director": {
        "ACTED_IN": 26879, "ARCHIVE_FOOTAGE_MAKER_OF": 275, "ARCHIVE_SOUND_MAKER_OF": 5, 
        "CINEMATOGRAPHER_OF": 3930, "COMPOSED": 766, "DIRECTED": 28534, "EDITED": 1940, 
        "PRODUCED": 13206, "PRODUCTION_DESIGNER_OF": 131381, "WROTE": 21320,
        "BORN_IN": 27370, "DIED_IN": 27370
    },
    "assistant": {
        "ACTED_IN": 1244, "ARCHIVE_FOOTAGE_MAKER_OF": 5, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 39, "COMPOSED": 15, "DIRECTED": 150, "EDITED": 36, 
        "PRODUCED": 181, "PRODUCTION_DESIGNER_OF": 7, "WROTE": 121,
        "BORN_IN": 443, "DIED_IN": 443
    },
    "assistant_director": {
        "ACTED_IN": 201443, "ARCHIVE_FOOTAGE_MAKER_OF": 1251, "ARCHIVE_SOUND_MAKER_OF": 9, 
        "CINEMATOGRAPHER_OF": 36133, "COMPOSED": 4361, "DIRECTED": 752330, "EDITED": 41134, 
        "PRODUCED": 127485, "PRODUCTION_DESIGNER_OF": 4115, "WROTE": 135658,
        "BORN_IN": 84613, "DIED_IN": 84613
    },
    "camera_department": {
        "ACTED_IN": 261744, "ARCHIVE_FOOTAGE_MAKER_OF": 4528, "ARCHIVE_SOUND_MAKER_OF": 22, 
        "CINEMATOGRAPHER_OF": 910837, "COMPOSED": 8254, "DIRECTED": 248283, "EDITED": 100132, 
        "PRODUCED": 97848, "PRODUCTION_DESIGNER_OF": 5897, "WROTE": 50819,
        "BORN_IN": 186421, "DIED_IN": 186421
    },
    "casting_department": {
        "ACTED_IN": 71426, "ARCHIVE_FOOTAGE_MAKER_OF": 318, "ARCHIVE_SOUND_MAKER_OF": 7, 
        "CINEMATOGRAPHER_OF": 840, "COMPOSED": 404, "DIRECTED": 11007, "EDITED": 2859, 
        "PRODUCED": 34346, "PRODUCTION_DESIGNER_OF": 440, "WROTE": 8779,
        "BORN_IN": 13843, "DIED_IN": 13843
    },
    "casting_director": {
        "ACTED_IN": 80137, "ARCHIVE_FOOTAGE_MAKER_OF": 372, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 439, "COMPOSED": 209, "DIRECTED": 20845, "EDITED": 1418, 
        "PRODUCED": 23864, "PRODUCTION_DESIGNER_OF": 250, "WROTE": 12149,
        "BORN_IN": 10628, "DIED_IN": 10628
    },
    "cinematographer": {
        "ACTED_IN": 137324, "ARCHIVE_FOOTAGE_MAKER_OF": 1444, "ARCHIVE_SOUND_MAKER_OF": 11, 
        "CINEMATOGRAPHER_OF": 1367616, "COMPOSED": 6642, "DIRECTED": 352706, "EDITED": 51109, 
        "PRODUCED": 79830, "PRODUCTION_DESIGNER_OF": 2074, "WROTE": 44313,
        "BORN_IN": 284302, "DIED_IN": 284302
    },
    "composer": {
        "ACTED_IN": 477897, "ARCHIVE_FOOTAGE_MAKER_OF": 10834, "ARCHIVE_SOUND_MAKER_OF": 69, 
        "CINEMATOGRAPHER_OF": 4279, "COMPOSED": 1413197, "DIRECTED": 27430, "EDITED": 8500, 
        "PRODUCED": 16353, "PRODUCTION_DESIGNER_OF": 409, "WROTE": 45299,
        "BORN_IN": 248066, "DIED_IN": 248066
    },
    "costume_department": {
        "ACTED_IN": 60019, "ARCHIVE_FOOTAGE_MAKER_OF": 650, "ARCHIVE_SOUND_MAKER_OF": 18, 
        "CINEMATOGRAPHER_OF": 628, "COMPOSED": 277, "DIRECTED": 3703, "EDITED": 1382, 
        "PRODUCED": 6099, "PRODUCTION_DESIGNER_OF": 6829, "WROTE": 8415,
        "BORN_IN": 14904, "DIED_IN": 14904
    },
    "costume_designer": {
        "ACTED_IN": 36504, "ARCHIVE_FOOTAGE_MAKER_OF": 246, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 351, "COMPOSED": 203, "DIRECTED": 4283, "EDITED": 431, 
        "PRODUCED": 3052, "PRODUCTION_DESIGNER_OF": 15531, "WROTE": 3793,
        "BORN_IN": 11048, "DIED_IN": 11048
    },
    "director": {
        "ACTED_IN": 2315792, "ARCHIVE_FOOTAGE_MAKER_OF": 27118, "ARCHIVE_SOUND_MAKER_OF": 205, 
        "CINEMATOGRAPHER_OF": 267819, "COMPOSED": 21866, "DIRECTED": 4398352, "EDITED": 175106, 
        "PRODUCED": 562157, "PRODUCTION_DESIGNER_OF": 11864, "WROTE": 883586,
        "BORN_IN": 560717, "DIED_IN": 560717
    },
    "editor": {
        "ACTED_IN": 229937, "ARCHIVE_FOOTAGE_MAKER_OF": 1428, "ARCHIVE_SOUND_MAKER_OF": 29, 
        "CINEMATOGRAPHER_OF": 114850, "COMPOSED": 15178, "DIRECTED": 449208, "EDITED": 1326183, 
        "PRODUCED": 106401, "PRODUCTION_DESIGNER_OF": 1874, "WROTE": 101144,
        "BORN_IN": 257000, "DIED_IN": 257000
    },
    "editorial_department": {
        "ACTED_IN": 62326, "ARCHIVE_FOOTAGE_MAKER_OF": 472, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 42337, "COMPOSED": 4202, "DIRECTED": 76548, "EDITED": 682261, 
        "PRODUCED": 59430, "PRODUCTION_DESIGNER_OF": 902, "WROTE": 37219,
        "BORN_IN": 63380, "DIED_IN": 63380
    },
    "electrical_department": {
        "ACTED_IN": 83, "ARCHIVE_FOOTAGE_MAKER_OF": 0, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 0, "COMPOSED": 0, "DIRECTED": 0, "EDITED": 1, 
        "PRODUCED": 0, "PRODUCTION_DESIGNER_OF": 0, "WROTE": 0,
        "BORN_IN": 2, "DIED_IN": 2
    },
    "executive": {
        "ACTED_IN": 46081, "ARCHIVE_FOOTAGE_MAKER_OF": 1293, "ARCHIVE_SOUND_MAKER_OF": 16, 
        "CINEMATOGRAPHER_OF": 757, "COMPOSED": 498, "DIRECTED": 3068, "EDITED": 563, 
        "PRODUCED": 54632, "PRODUCTION_DESIGNER_OF": 133, "WROTE": 14571,
        "BORN_IN": 9007, "DIED_IN": 9007
    },
    "legal": {
        "ACTED_IN": 2007, "ARCHIVE_FOOTAGE_MAKER_OF": 49, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 6, "COMPOSED": 10, "DIRECTED": 2593, "EDITED": 5, 
        "PRODUCED": 507, "PRODUCTION_DESIGNER_OF": 0, "WROTE": 631,
        "BORN_IN": 437, "DIED_IN": 437
    },
    "location_management": {
        "ACTED_IN": 26248, "ARCHIVE_FOOTAGE_MAKER_OF": 112, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 3081, "COMPOSED": 602, "DIRECTED": 22452, "EDITED": 1620, 
        "PRODUCED": 28478, "PRODUCTION_DESIGNER_OF": 1703, "WROTE": 9631,
        "BORN_IN": 13050, "DIED_IN": 13050
    },
    "make_up_department": {
        "ACTED_IN": 77505, "ARCHIVE_FOOTAGE_MAKER_OF": 1038, "ARCHIVE_SOUND_MAKER_OF": 3, 
        "CINEMATOGRAPHER_OF": 1213, "COMPOSED": 1474, "DIRECTED": 5202, "EDITED": 1270, 
        "PRODUCED": 5213, "PRODUCTION_DESIGNER_OF": 2719, "WROTE": 4238,
        "BORN_IN": 18686, "DIED_IN": 18686
    },
    "manager": {
        "ACTED_IN": 11227, "ARCHIVE_FOOTAGE_MAKER_OF": 83, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 238, "COMPOSED": 445, "DIRECTED": 788, "EDITED": 199, 
        "PRODUCED": 11321, "PRODUCTION_DESIGNER_OF": 62, "WROTE": 2710,
        "BORN_IN": 3122, "DIED_IN": 3122
    },
    "miscellaneous": {
        "ACTED_IN": 1338470, "ARCHIVE_FOOTAGE_MAKER_OF": 15642, "ARCHIVE_SOUND_MAKER_OF": 310, 
        "CINEMATOGRAPHER_OF": 90087, "COMPOSED": 21122, "DIRECTED": 491294, "EDITED": 117573, 
        "PRODUCED": 609647, "PRODUCTION_DESIGNER_OF": 17759, "WROTE": 1204892,
        "BORN_IN": 228889, "DIED_IN": 228889
    },
    "music_department": {
        "ACTED_IN": 608627, "ARCHIVE_FOOTAGE_MAKER_OF": 9186, "ARCHIVE_SOUND_MAKER_OF": 189, 
        "CINEMATOGRAPHER_OF": 2511, "COMPOSED": 955171, "DIRECTED": 18409, "EDITED": 15018, 
        "PRODUCED": 23633, "PRODUCTION_DESIGNER_OF": 175, "WROTE": 115410,
        "BORN_IN": 76607, "DIED_IN": 76607
    },
    "producer": {
        "ACTED_IN": 3852407, "ARCHIVE_FOOTAGE_MAKER_OF": 42086, "ARCHIVE_SOUND_MAKER_OF": 544, 
        "CINEMATOGRAPHER_OF": 179006, "COMPOSED": 57855, "DIRECTED": 1743713, "EDITED": 210501, 
        "PRODUCED": 2464941, "PRODUCTION_DESIGNER_OF": 25152, "WROTE": 2014325,
        "BORN_IN": 613186, "DIED_IN": 613186
    },
    "production_department": {
        "ACTED_IN": 0, "ARCHIVE_FOOTAGE_MAKER_OF": 0, "ARCHIVE_SOUND_MAKER_OF": 6, 
        "CINEMATOGRAPHER_OF": 0, "COMPOSED": 0, "DIRECTED": 0, "EDITED": 0, 
        "PRODUCED": 1, "PRODUCTION_DESIGNER_OF": 276145, "WROTE": 0,
        "BORN_IN": 1, "DIED_IN": 1
    },
    "production_designer": {
        "ACTED_IN": 26731, "ARCHIVE_FOOTAGE_MAKER_OF": 181, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 2728, "COMPOSED": 726, "DIRECTED": 21996, "EDITED": 1633, 
        "PRODUCED": 17017, "PRODUCTION_DESIGNER_OF": 0, "WROTE": 15902,
        "BORN_IN": 51274, "DIED_IN": 51274
    },
    "production_manager": {
        "ACTED_IN": 74967, "ARCHIVE_FOOTAGE_MAKER_OF": 1052, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 7553, "COMPOSED": 1996, "DIRECTED": 87105, "EDITED": 30298, 
        "PRODUCED": 338896, "PRODUCTION_DESIGNER_OF": 3106, "WROTE": 64513,
        "BORN_IN": 51119, "DIED_IN": 51119
    },
    "publicist": {
        "ACTED_IN": 2679, "ARCHIVE_FOOTAGE_MAKER_OF": 105, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 9, "COMPOSED": 36, "DIRECTED": 162, "EDITED": 25, 
        "PRODUCED": 773, "PRODUCTION_DESIGNER_OF": 11, "WROTE": 224,
        "BORN_IN": 581, "DIED_IN": 581
    },
    "script_department": {
        "ACTED_IN": 63521, "ARCHIVE_FOOTAGE_MAKER_OF": 452, "ARCHIVE_SOUND_MAKER_OF": 11, 
        "CINEMATOGRAPHER_OF": 1835, "COMPOSED": 1027, "DIRECTED": 48371, "EDITED": 11327, 
        "PRODUCED": 46905, "PRODUCTION_DESIGNER_OF": 546, "WROTE": 355616,
        "BORN_IN": 21987, "DIED_IN": 21987
    },
    "set_decorator": {
        "ACTED_IN": 13091, "ARCHIVE_FOOTAGE_MAKER_OF": 55, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 955, "COMPOSED": 311, "DIRECTED": 6767, "EDITED": 711, 
        "PRODUCED": 2587, "PRODUCTION_DESIGNER_OF": 36206, "WROTE": 1550,
        "BORN_IN": 9893, "DIED_IN": 9893
    },
    "sound_department": {
        "ACTED_IN": 184110, "ARCHIVE_FOOTAGE_MAKER_OF": 509, "ARCHIVE_SOUND_MAKER_OF": 66, 
        "CINEMATOGRAPHER_OF": 37334, "COMPOSED": 159926, "DIRECTED": 52031, "EDITED": 107218, 
        "PRODUCED": 35229, "PRODUCTION_DESIGNER_OF": 1952, "WROTE": 22699,
        "BORN_IN": 80900, "DIED_IN": 80900
    },
    "soundtrack": {
        "ACTED_IN": 3260775, "ARCHIVE_FOOTAGE_MAKER_OF": 52102, "ARCHIVE_SOUND_MAKER_OF": 726, 
        "CINEMATOGRAPHER_OF": 1116, "COMPOSED": 628532, "DIRECTED": 24857, "EDITED": 1756, 
        "PRODUCED": 17336, "PRODUCTION_DESIGNER_OF": 106, "WROTE": 142990,
        "BORN_IN": 99799, "DIED_IN": 99799
    },
    "special_effects": {
        "ACTED_IN": 30578, "ARCHIVE_FOOTAGE_MAKER_OF": 189, "ARCHIVE_SOUND_MAKER_OF": 1, 
        "CINEMATOGRAPHER_OF": 11683, "COMPOSED": 1086, "DIRECTED": 6461, "EDITED": 7784, 
        "PRODUCED": 3026, "PRODUCTION_DESIGNER_OF": 3752, "WROTE": 2383,
        "BORN_IN": 11232, "DIED_IN": 11232
    },
    "stunts": {
        "ACTED_IN": 172580, "ARCHIVE_FOOTAGE_MAKER_OF": 1333, "ARCHIVE_SOUND_MAKER_OF": 14, 
        "CINEMATOGRAPHER_OF": 1388, "COMPOSED": 339, "DIRECTED": 8071, "EDITED": 545, 
        "PRODUCED": 9604, "PRODUCTION_DESIGNER_OF": 135, "WROTE": 2961,
        "BORN_IN": 21182, "DIED_IN": 21182
    },
    "talent_agent": {
        "ACTED_IN": 17490, "ARCHIVE_FOOTAGE_MAKER_OF": 187, "ARCHIVE_SOUND_MAKER_OF": 5, 
        "CINEMATOGRAPHER_OF": 154, "COMPOSED": 200, "DIRECTED": 481, "EDITED": 4531, 
        "PRODUCED": 5823, "PRODUCTION_DESIGNER_OF": 18, "WROTE": 906,
        "BORN_IN": 2291, "DIED_IN": 2291
    },
    "transportation_department": {
        "ACTED_IN": 13190, "ARCHIVE_FOOTAGE_MAKER_OF": 154, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 1467, "COMPOSED": 367, "DIRECTED": 870, "EDITED": 809, 
        "PRODUCED": 3125, "PRODUCTION_DESIGNER_OF": 473, "WROTE": 1223,
        "BORN_IN": 4459, "DIED_IN": 4459
    },
    "visual_effects": {
        "ACTED_IN": 40185, "ARCHIVE_FOOTAGE_MAKER_OF": 270, "ARCHIVE_SOUND_MAKER_OF": 6, 
        "CINEMATOGRAPHER_OF": 29654, "COMPOSED": 3212, "DIRECTED": 43382, "EDITED": 67190, 
        "PRODUCED": 18737, "PRODUCTION_DESIGNER_OF": 5920, "WROTE": 12263,
        "BORN_IN": 36300, "DIED_IN": 36300
    },
    "writer": {
        "ACTED_IN": 3960419, "ARCHIVE_FOOTAGE_MAKER_OF": 38793, "ARCHIVE_SOUND_MAKER_OF": 634, 
        "CINEMATOGRAPHER_OF": 78420, "COMPOSED": 31832, "DIRECTED": 1853560, "EDITED": 99018, 
        "PRODUCED": 607136, "PRODUCTION_DESIGNER_OF": 8472, "WROTE": 5319043,
        "BORN_IN": 683795, "DIED_IN": 683795
    }
}

# Deklarasi jumlah relasi MASUK (Incoming) ke entitas Film/Movie
incoming_rel_counts = {
    "action": {
        "ACTED_IN": 1230882, "ARCHIVE_FOOTAGE_MAKER_OF": 4785, "ARCHIVE_SOUND_MAKER_OF": 488, 
        "CINEMATOGRAPHER_OF": 66783, "COMPOSED": 115827, "DIRECTED": 271042, "EDITED": 50525, 
        "PRODUCED": 152468, "PRODUCTION_DESIGNER_OF": 10270, "WROTE": 426348
    },
    "adult": {
        "ACTED_IN": 783767, "ARCHIVE_FOOTAGE_MAKER_OF": 43237, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 9538, "COMPOSED": 5641, "DIRECTED": 73531, "EDITED": 14117, 
        "PRODUCED": 11023, "PRODUCTION_DESIGNER_OF": 431, "WROTE": 8735
    },
    "adventure": {
        "ACTED_IN": 1056053, "ARCHIVE_FOOTAGE_MAKER_OF": 3497, "ARCHIVE_SOUND_MAKER_OF": 373, 
        "CINEMATOGRAPHER_OF": 60371, "COMPOSED": 104922, "DIRECTED": 249591, "EDITED": 55016, 
        "PRODUCED": 127305, "PRODUCTION_DESIGNER_OF": 10913, "WROTE": 398140
    },
    "animation": {
        "ACTED_IN": 1017184, "ARCHIVE_FOOTAGE_MAKER_OF": 1866, "ARCHIVE_SOUND_MAKER_OF": 790, 
        "CINEMATOGRAPHER_OF": 27525, "COMPOSED": 131642, "DIRECTED": 304392, "EDITED": 55299, 
        "PRODUCED": 132947, "PRODUCTION_DESIGNER_OF": 6086, "WROTE": 395706
    },
    "biography": {
        "ACTED_IN": 187118, "ARCHIVE_FOOTAGE_MAKER_OF": 8731, "ARCHIVE_SOUND_MAKER_OF": 26, 
        "CINEMATOGRAPHER_OF": 24552, "COMPOSED": 21975, "DIRECTED": 59948, "EDITED": 21419, 
        "PRODUCED": 32828, "PRODUCTION_DESIGNER_OF": 2663, "WROTE": 41963
    },
    "comedy": {
        "ACTED_IN": 5776115, "ARCHIVE_FOOTAGE_MAKER_OF": 23252, "ARCHIVE_SOUND_MAKER_OF": 691, 
        "CINEMATOGRAPHER_OF": 312480, "COMPOSED": 334011, "DIRECTED": 1126831, "EDITED": 274400, 
        "PRODUCED": 583231, "PRODUCTION_DESIGNER_OF": 88423, "WROTE": 1668482
    },
    "crime": {
        "ACTED_IN": 1264641, "ARCHIVE_FOOTAGE_MAKER_OF": 1773, "ARCHIVE_SOUND_MAKER_OF": 18, 
        "CINEMATOGRAPHER_OF": 91877, "COMPOSED": 109847, "DIRECTED": 294318, "EDITED": 69317, 
        "PRODUCED": 187252, "PRODUCTION_DESIGNER_OF": 20048, "WROTE": 491454
    },
    "documentary": {
        "ACTED_IN": 827125, "ARCHIVE_FOOTAGE_MAKER_OF": 45518, "ARCHIVE_SOUND_MAKER_OF": 243, 
        "CINEMATOGRAPHER_OF": 232968, "COMPOSED": 152376, "DIRECTED": 435655, "EDITED": 239358, 
        "PRODUCED": 243383, "PRODUCTION_DESIGNER_OF": 7200, "WROTE": 151441
    },
    "drama": {
        "ACTED_IN": 8160487, "ARCHIVE_FOOTAGE_MAKER_OF": 5524, "ARCHIVE_SOUND_MAKER_OF": 27, 
        "CINEMATOGRAPHER_OF": 581332, "COMPOSED": 531594, "DIRECTED": 2082743, "EDITED": 390703, 
        "PRODUCED": 996207, "PRODUCTION_DESIGNER_OF": 137329, "WROTE": 2854122
    },
    "family": {
        "ACTED_IN": 1745818, "ARCHIVE_FOOTAGE_MAKER_OF": 4386, "ARCHIVE_SOUND_MAKER_OF": 252, 
        "CINEMATOGRAPHER_OF": 94191, "COMPOSED": 134427, "DIRECTED": 397648, "EDITED": 108511, 
        "PRODUCED": 217841, "PRODUCTION_DESIGNER_OF": 26433, "WROTE": 512868
    },
    "fantasy": {
        "ACTED_IN": 559487, "ARCHIVE_FOOTAGE_MAKER_OF": 1082, "ARCHIVE_SOUND_MAKER_OF": 88, 
        "CINEMATOGRAPHER_OF": 40087, "COMPOSED": 54850, "DIRECTED": 144474, "EDITED": 27473, 
        "PRODUCED": 72054, "PRODUCTION_DESIGNER_OF": 10072, "WROTE": 189413
    },
    "film_noir": {
        "ACTED_IN": 3212, "ARCHIVE_FOOTAGE_MAKER_OF": 0, "ARCHIVE_SOUND_MAKER_OF": 0, 
        "CINEMATOGRAPHER_OF": 548, "COMPOSED": 524, "DIRECTED": 785, "EDITED": 289, 
        "PRODUCED": 537, "PRODUCTION_DESIGNER_OF": 9, "WROTE": 1839
    },
    "game_show": {
        "ACTED_IN": 763616, "ARCHIVE_FOOTAGE_MAKER_OF": 2568, "ARCHIVE_SOUND_MAKER_OF": 22, 
        "CINEMATOGRAPHER_OF": 6921, "COMPOSED": 36456, "DIRECTED": 92006, "EDITED": 53798, 
        "PRODUCED": 83862, "PRODUCTION_DESIGNER_OF": 15475, "WROTE": 81622
    },
    "history": {
        "ACTED_IN": 273944, "ARCHIVE_FOOTAGE_MAKER_OF": 6802, "ARCHIVE_SOUND_MAKER_OF": 192, 
        "CINEMATOGRAPHER_OF": 32258, "COMPOSED": 30959, "DIRECTED": 75873, "EDITED": 27832, 
        "PRODUCED": 39707, "PRODUCTION_DESIGNER_OF": 4932, "WROTE": 71522
    },
    "horror": {
        "ACTED_IN": 440395, "ARCHIVE_FOOTAGE_MAKER_OF": 1421, "ARCHIVE_SOUND_MAKER_OF": 51, 
        "CINEMATOGRAPHER_OF": 49089, "COMPOSED": 48903, "DIRECTED": 104942, "EDITED": 24745, 
        "PRODUCED": 65930, "PRODUCTION_DESIGNER_OF": 9056, "WROTE": 96393
    },
    "music": {
        "ACTED_IN": 1199835, "ARCHIVE_FOOTAGE_MAKER_OF": 17184, "ARCHIVE_SOUND_MAKER_OF": 96, 
        "CINEMATOGRAPHER_OF": 54276, "COMPOSED": 64896, "DIRECTED": 219984, "EDITED": 61038, 
        "PRODUCED": 97101, "PRODUCTION_DESIGNER_OF": 16573, "WROTE": 191400
    },
    "musical": {
        "ACTED_IN": 195107, "ARCHIVE_FOOTAGE_MAKER_OF": 1090, "ARCHIVE_SOUND_MAKER_OF": 29, 
        "CINEMATOGRAPHER_OF": 14317, "COMPOSED": 16231, "DIRECTED": 50900, "EDITED": 10490, 
        "PRODUCED": 25287, "PRODUCTION_DESIGNER_OF": 3205, "WROTE": 51533
    },
    "mystery": {
        "ACTED_IN": 589673, "ARCHIVE_FOOTAGE_MAKER_OF": 936, "ARCHIVE_SOUND_MAKER_OF": 22, 
        "CINEMATOGRAPHER_OF": 42557, "COMPOSED": 55619, "DIRECTED": 137654, "EDITED": 25934, 
        "PRODUCED": 85544, "PRODUCTION_DESIGNER_OF": 7792, "WROTE": 210391
    },
    "news": {
        "ACTED_IN": 859718, "ARCHIVE_FOOTAGE_MAKER_OF": 31387, "ARCHIVE_SOUND_MAKER_OF": 368, 
        "CINEMATOGRAPHER_OF": 13630, "COMPOSED": 63605, "DIRECTED": 75972, "EDITED": 60097, 
        "PRODUCED": 97180, "PRODUCTION_DESIGNER_OF": 3682, "WROTE": 105562
    },
    "reality_tv": {
        "ACTED_IN": 731951, "ARCHIVE_FOOTAGE_MAKER_OF": 2854, "ARCHIVE_SOUND_MAKER_OF": 11, 
        "CINEMATOGRAPHER_OF": 68900, "COMPOSED": 83171, "DIRECTED": 146031, "EDITED": 183762, 
        "PRODUCED": 158576, "PRODUCTION_DESIGNER_OF": 10540, "WROTE": 98896
    },
    "romance": {
        "ACTED_IN": 2907409, "ARCHIVE_FOOTAGE_MAKER_OF": 1524, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 118989, "COMPOSED": 127344, "DIRECTED": 759546, "EDITED": 92229, 
        "PRODUCED": 284671, "PRODUCTION_DESIGNER_OF": 37873, "WROTE": 1160519
    },
    "sci_fi": {
        "ACTED_IN": 325339, "ARCHIVE_FOOTAGE_MAKER_OF": 1483, "ARCHIVE_SOUND_MAKER_OF": 221, 
        "CINEMATOGRAPHER_OF": 27678, "COMPOSED": 34105, "DIRECTED": 70932, "EDITED": 17905, 
        "PRODUCED": 44965, "PRODUCTION_DESIGNER_OF": 6726, "WROTE": 81271
    },
    "sport": {
        "ACTED_IN": 371509, "ARCHIVE_FOOTAGE_MAKER_OF": 10718, "ARCHIVE_SOUND_MAKER_OF": 291, 
        "CINEMATOGRAPHER_OF": 17335, "COMPOSED": 16167, "DIRECTED": 43658, "EDITED": 28227, 
        "PRODUCED": 40037, "PRODUCTION_DESIGNER_OF": 2332, "WROTE": 46891
    },
    "talk_show": {
        "ACTED_IN": 1979368, "ARCHIVE_FOOTAGE_MAKER_OF": 28929, "ARCHIVE_SOUND_MAKER_OF": 396, 
        "CINEMATOGRAPHER_OF": 21735, "COMPOSED": 49909, "DIRECTED": 161568, "EDITED": 98220, 
        "PRODUCED": 148124, "PRODUCTION_DESIGNER_OF": 11796, "WROTE": 261408
    },
    "thriller": {
        "ACTED_IN": 472757, "ARCHIVE_FOOTAGE_MAKER_OF": 296, "ARCHIVE_SOUND_MAKER_OF": 5, 
        "CINEMATOGRAPHER_OF": 50177, "COMPOSED": 51880, "DIRECTED": 121988, "EDITED": 29195, 
        "PRODUCED": 79100, "PRODUCTION_DESIGNER_OF": 9267, "WROTE": 136357
    },
    "war": {
        "ACTED_IN": 95675, "ARCHIVE_FOOTAGE_MAKER_OF": 952, "ARCHIVE_SOUND_MAKER_OF": 33, 
        "CINEMATOGRAPHER_OF": 12134, "COMPOSED": 11245, "DIRECTED": 24055, "EDITED": 8408, 
        "PRODUCED": 12472, "PRODUCTION_DESIGNER_OF": 2513, "WROTE": 29409
    },
    "western": {
        "ACTED_IN": 112634, "ARCHIVE_FOOTAGE_MAKER_OF": 680, "ARCHIVE_SOUND_MAKER_OF": 4, 
        "CINEMATOGRAPHER_OF": 14239, "COMPOSED": 9330, "DIRECTED": 23891, "EDITED": 9135, 
        "PRODUCED": 15302, "PRODUCTION_DESIGNER_OF": 635, "WROTE": 36782
    }
}

# Deklarasi jumlah relasi KELUAR (Outgoing) dari entitas Movie
movie_outgoing_rel_counts = {
    "action": {"HAS_CATEGORY": 293467, "RELEASED_IN": 293467},
    "adult": {"HAS_CATEGORY": 222819, "RELEASED_IN": 222819},
    "adventure": {"HAS_CATEGORY": 273401, "RELEASED_IN": 273401},
    "animation": {"HAS_CATEGORY": 330135, "RELEASED_IN": 330135},
    "biography": {"HAS_CATEGORY": 76749, "RELEASED_IN": 76749},
    "comedy": {"HAS_CATEGORY": 1479294, "RELEASED_IN": 1479294},
    "crime": {"HAS_CATEGORY": 312629, "RELEASED_IN": 312629},
    "documentary": {"HAS_CATEGORY": 618520, "RELEASED_IN": 618520},
    "drama": {"HAS_CATEGORY": 1984332, "RELEASED_IN": 1984332},
    "family": {"HAS_CATEGORY": 489281, "RELEASED_IN": 489281},
    "fantasy": {"HAS_CATEGORY": 155302, "RELEASED_IN": 155302},
    "film_noir": {"HAS_CATEGORY": 784, "RELEASED_IN": 784},
    "game_show": {"HAS_CATEGORY": 225632, "RELEASED_IN": 225632},
    "history": {"HAS_CATEGORY": 95891, "RELEASED_IN": 95891},
    "horror": {"HAS_CATEGORY": 130261, "RELEASED_IN": 130261},
    "music": {"HAS_CATEGORY": 356267, "RELEASED_IN": 356267},
    "musical": {"HAS_CATEGORY": 54325, "RELEASED_IN": 54325},
    "mystery": {"HAS_CATEGORY": 149470, "RELEASED_IN": 149470},
    "news": {"HAS_CATEGORY": 408975, "RELEASED_IN": 408975},
    "reality_tv": {"HAS_CATEGORY": 338752, "RELEASED_IN": 338752},
    "romance": {"HAS_CATEGORY": 644609, "RELEASED_IN": 644609},
    "sci_fi": {"HAS_CATEGORY": 89121, "RELEASED_IN": 89121},
    "sport": {"HAS_CATEGORY": 137057, "RELEASED_IN": 137057},
    "talk_show": {"HAS_CATEGORY": 773293, "RELEASED_IN": 773293},
    "thriller": {"HAS_CATEGORY": 124666, "RELEASED_IN": 124666},
    "war": {"HAS_CATEGORY": 26911, "RELEASED_IN": 26911},
    "western": {"HAS_CATEGORY": 26970, "RELEASED_IN": 26970}
}
outgoing_rel_counts.update(movie_outgoing_rel_counts)

# Deklarasi jumlah relasi MASUK (Incoming) ke entitas Category
category_incoming_rel_counts = {
    "audiobook": {"HAS_CATEGORY": 1},
    "episode": {"HAS_CATEGORY": 1},
    "movie": {"HAS_CATEGORY": 492210},
    "radioSeries": {"HAS_CATEGORY": 1},
    "short": {"HAS_CATEGORY": 639766},
    "tvEpisode": {"HAS_CATEGORY": 4587657},
    "tvMiniSeries": {"HAS_CATEGORY": 28085},
    "tvMovie": {"HAS_CATEGORY": 116975},
    "tvSeries": {"HAS_CATEGORY": 162227},
    "tvShort": {"HAS_CATEGORY": 7633},
    "tvSpecial": {"HAS_CATEGORY": 26082},
    "video": {"HAS_CATEGORY": 265757},
    "videoGame": {"HAS_CATEGORY": 15693}
}
incoming_rel_counts.update(category_incoming_rel_counts)

year_incoming_rel_counts = {
    "year_2115": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_2028": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_2027": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 5},
    "year_2026": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 4},
    "year_2025": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 8},
    "year_2024": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 41},
    "year_2023": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 161},
    "year_2022": {"BORN_IN": 0, "DIED_IN": 0, "RELEASED_IN": 1869},
    "year_2021": {"BORN_IN": 0, "DIED_IN": 655, "RELEASED_IN": 53493},
    "year_2020": {"BORN_IN": 1, "DIED_IN": 3510, "RELEASED_IN": 240885},
    "year_2019": {"BORN_IN": 1, "DIED_IN": 3124, "RELEASED_IN": 293391},
    "year_2018": {"BORN_IN": 0, "DIED_IN": 3118, "RELEASED_IN": 309713},
    "year_2017": {"BORN_IN": 2, "DIED_IN": 3123, "RELEASED_IN": 326849},
    "year_2016": {"BORN_IN": 6, "DIED_IN": 3218, "RELEASED_IN": 315054},
    "year_2015": {"BORN_IN": 4, "DIED_IN": 3116, "RELEASED_IN": 301687},
    "year_2014": {"BORN_IN": 15, "DIED_IN": 2981, "RELEASED_IN": 286661},
    "year_2013": {"BORN_IN": 15, "DIED_IN": 2921, "RELEASED_IN": 274407},
    "year_2012": {"BORN_IN": 32, "DIED_IN": 2953, "RELEASED_IN": 256827},
    "year_2011": {"BORN_IN": 39, "DIED_IN": 2875, "RELEASED_IN": 230219},
    "year_2010": {"BORN_IN": 61, "DIED_IN": 2775, "RELEASED_IN": 201811},
    "year_2009": {"BORN_IN": 77, "DIED_IN": 2711, "RELEASED_IN": 178162},
    "year_2008": {"BORN_IN": 98, "DIED_IN": 2619, "RELEASED_IN": 166310},
    "year_2007": {"BORN_IN": 132, "DIED_IN": 2442, "RELEASED_IN": 154677},
    "year_2006": {"BORN_IN": 138, "DIED_IN": 2491, "RELEASED_IN": 139569},
    "year_2005": {"BORN_IN": 196, "DIED_IN": 2348, "RELEASED_IN": 124040},
    "year_2004": {"BORN_IN": 246, "DIED_IN": 2337, "RELEASED_IN": 110667},
    "year_2003": {"BORN_IN": 320, "DIED_IN": 2288, "RELEASED_IN": 96314},
    "year_2002": {"BORN_IN": 393, "DIED_IN": 2094, "RELEASED_IN": 82362},
    "year_2001": {"BORN_IN": 554, "DIED_IN": 2090, "RELEASED_IN": 78922},
    "year_2000": {"BORN_IN": 674, "DIED_IN": 1938, "RELEASED_IN": 70977},
    "year_1999": {"BORN_IN": 900, "DIED_IN": 2011, "RELEASED_IN": 68290},
    "year_1998": {"BORN_IN": 1259, "DIED_IN": 1857, "RELEASED_IN": 64196},
    "year_1997": {"BORN_IN": 1574, "DIED_IN": 1827, "RELEASED_IN": 57892},
    "year_1996": {"BORN_IN": 1739, "DIED_IN": 1842, "RELEASED_IN": 54464},
    "year_1995": {"BORN_IN": 2055, "DIED_IN": 1878, "RELEASED_IN": 52210},
    "year_1994": {"BORN_IN": 2280, "DIED_IN": 1731, "RELEASED_IN": 46553},
    "year_1993": {"BORN_IN": 2619, "DIED_IN": 1813, "RELEASED_IN": 41693},
    "year_1992": {"BORN_IN": 3006, "DIED_IN": 1754, "RELEASED_IN": 39291},
    "year_1991": {"BORN_IN": 3196, "DIED_IN": 1706, "RELEASED_IN": 38592},
    "year_1990": {"BORN_IN": 3686, "DIED_IN": 1654, "RELEASED_IN": 36334},
    "year_1989": {"BORN_IN": 3956, "DIED_IN": 1652, "RELEASED_IN": 34805},
    "year_1988": {"BORN_IN": 4415, "DIED_IN": 1552, "RELEASED_IN": 32144},
    "year_1987": {"BORN_IN": 4682, "DIED_IN": 1469, "RELEASED_IN": 31942},
    "year_1986": {"BORN_IN": 5234, "DIED_IN": 1474, "RELEASED_IN": 29350},
    "year_1985": {"BORN_IN": 5397, "DIED_IN": 1455, "RELEASED_IN": 29538},
    "year_1984": {"BORN_IN": 5756, "DIED_IN": 1505, "RELEASED_IN": 27142},
    "year_1983": {"BORN_IN": 5646, "DIED_IN": 1432, "RELEASED_IN": 25930},
    "year_1982": {"BORN_IN": 6192, "DIED_IN": 1356, "RELEASED_IN": 25526},
    "year_1981": {"BORN_IN": 6195, "DIED_IN": 1333, "RELEASED_IN": 24159},
    "year_1980": {"BORN_IN": 6439, "DIED_IN": 1387, "RELEASED_IN": 24492},
    "year_1979": {"BORN_IN": 6302, "DIED_IN": 1335, "RELEASED_IN": 22438},
    "year_1978": {"BORN_IN": 6358, "DIED_IN": 1216, "RELEASED_IN": 22332},
    "year_1977": {"BORN_IN": 5926, "DIED_IN": 1195, "RELEASED_IN": 22499},
    "year_1976": {"BORN_IN": 5852, "DIED_IN": 1152, "RELEASED_IN": 22926},
    "year_1975": {"BORN_IN": 5722, "DIED_IN": 1166, "RELEASED_IN": 23033},
    "year_1974": {"BORN_IN": 5717, "DIED_IN": 1136, "RELEASED_IN": 23132},
    "year_1973": {"BORN_IN": 5376, "DIED_IN": 1187, "RELEASED_IN": 23934},
    "year_1972": {"BORN_IN": 5544, "DIED_IN": 1075, "RELEASED_IN": 22670},
    "year_1971": {"BORN_IN": 5481, "DIED_IN": 1110, "RELEASED_IN": 22384},
    "year_1970": {"BORN_IN": 5587, "DIED_IN": 1086, "RELEASED_IN": 21686},
    "year_1969": {"BORN_IN": 5132, "DIED_IN": 1017, "RELEASED_IN": 21786},
    "year_1968": {"BORN_IN": 4830, "DIED_IN": 1035, "RELEASED_IN": 19427},
    "year_1967": {"BORN_IN": 4525, "DIED_IN": 1041, "RELEASED_IN": 20162},
    "year_1966": {"BORN_IN": 4463, "DIED_IN": 951, "RELEASED_IN": 19977},
    "year_1965": {"BORN_IN": 4572, "DIED_IN": 862, "RELEASED_IN": 18807},
    "year_1964": {"BORN_IN": 4565, "DIED_IN": 861, "RELEASED_IN": 16568},
    "year_1963": {"BORN_IN": 4325, "DIED_IN": 807, "RELEASED_IN": 15451},
    "year_1962": {"BORN_IN": 4281, "DIED_IN": 835, "RELEASED_IN": 13589},
    "year_1961": {"BORN_IN": 4123, "DIED_IN": 767, "RELEASED_IN": 14725},
    "year_1960": {"BORN_IN": 3885, "DIED_IN": 752, "RELEASED_IN": 14415},
    "year_1959": {"BORN_IN": 3745, "DIED_IN": 704, "RELEASED_IN": 13601},
    "year_1958": {"BORN_IN": 3765, "DIED_IN": 731, "RELEASED_IN": 13055},
    "year_1957": {"BORN_IN": 3677, "DIED_IN": 693, "RELEASED_IN": 12315},
    "year_1956": {"BORN_IN": 3387, "DIED_IN": 612, "RELEASED_IN": 11098},
    "year_1955": {"BORN_IN": 3508, "DIED_IN": 590, "RELEASED_IN": 11240},
    "year_1954": {"BORN_IN": 3354, "DIED_IN": 603, "RELEASED_IN": 10378},
    "year_1953": {"BORN_IN": 3388, "DIED_IN": 591, "RELEASED_IN": 8097},
    "year_1952": {"BORN_IN": 3470, "DIED_IN": 552, "RELEASED_IN": 7484},
    "year_1951": {"BORN_IN": 3373, "DIED_IN": 554, "RELEASED_IN": 7321},
    "year_1950": {"BORN_IN": 3529, "DIED_IN": 495, "RELEASED_IN": 5763},
    "year_1949": {"BORN_IN": 3537, "DIED_IN": 480, "RELEASED_IN": 4198},
    "year_1948": {"BORN_IN": 3725, "DIED_IN": 457, "RELEASED_IN": 2970},
    "year_1947": {"BORN_IN": 4050, "DIED_IN": 486, "RELEASED_IN": 2452},
    "year_1946": {"BORN_IN": 3769, "DIED_IN": 449, "RELEASED_IN": 2093},
    "year_1945": {"BORN_IN": 3373, "DIED_IN": 573, "RELEASED_IN": 1636},
    "year_1944": {"BORN_IN": 3604, "DIED_IN": 592, "RELEASED_IN": 1601},
    "year_1943": {"BORN_IN": 3569, "DIED_IN": 500, "RELEASED_IN": 1770},
    "year_1942": {"BORN_IN": 3382, "DIED_IN": 523, "RELEASED_IN": 1976},
    "year_1941": {"BORN_IN": 3263, "DIED_IN": 439, "RELEASED_IN": 2043},
    "year_1940": {"BORN_IN": 3262, "DIED_IN": 432, "RELEASED_IN": 2056},
    "year_1939": {"BORN_IN": 3148, "DIED_IN": 388, "RELEASED_IN": 2428},
    "year_1938": {"BORN_IN": 3168, "DIED_IN": 383, "RELEASED_IN": 2750},
    "year_1937": {"BORN_IN": 3043, "DIED_IN": 394, "RELEASED_IN": 2809},
    "year_1936": {"BORN_IN": 2922, "DIED_IN": 360, "RELEASED_IN": 2599},
    "year_1935": {"BORN_IN": 2828, "DIED_IN": 326, "RELEASED_IN": 2304},
    "year_1934": {"BORN_IN": 2896, "DIED_IN": 305, "RELEASED_IN": 2301},
    "year_1933": {"BORN_IN": 2754, "DIED_IN": 314, "RELEASED_IN": 2238},
    "year_1932": {"BORN_IN": 2916, "DIED_IN": 271, "RELEASED_IN": 2314},
    "year_1931": {"BORN_IN": 3030, "DIED_IN": 284, "RELEASED_IN": 2459},
    "year_1930": {"BORN_IN": 3211, "DIED_IN": 253, "RELEASED_IN": 2402},
    "year_1929": {"BORN_IN": 3126, "DIED_IN": 276, "RELEASED_IN": 2800},
    "year_1928": {"BORN_IN": 3111, "DIED_IN": 246, "RELEASED_IN": 2648},
    "year_1927": {"BORN_IN": 3021, "DIED_IN": 224, "RELEASED_IN": 2671},
    "year_1926": {"BORN_IN": 2940, "DIED_IN": 185, "RELEASED_IN": 2621},
    "year_1925": {"BORN_IN": 2890, "DIED_IN": 196, "RELEASED_IN": 2309},
    "year_1924": {"BORN_IN": 2829, "DIED_IN": 197, "RELEASED_IN": 2009},
    "year_1923": {"BORN_IN": 2688, "DIED_IN": 189, "RELEASED_IN": 1938},
    "year_1922": {"BORN_IN": 2598, "DIED_IN": 152, "RELEASED_IN": 2246},
    "year_1921": {"BORN_IN": 2594, "DIED_IN": 149, "RELEASED_IN": 2504},
    "year_1920": {"BORN_IN": 2576, "DIED_IN": 161, "RELEASED_IN": 2873},
    "year_1919": {"BORN_IN": 1962, "DIED_IN": 124, "RELEASED_IN": 2742},
    "year_1918": {"BORN_IN": 1941, "DIED_IN": 160, "RELEASED_IN": 3220},
    "year_1917": {"BORN_IN": 1752, "DIED_IN": 107, "RELEASED_IN": 4015},
    "year_1916": {"BORN_IN": 1798, "DIED_IN": 123, "RELEASED_IN": 5105},
    "year_1915": {"BORN_IN": 1801, "DIED_IN": 101, "RELEASED_IN": 6538},
    "year_1914": {"BORN_IN": 1978, "DIED_IN": 74, "RELEASED_IN": 6669},
    "year_1913": {"BORN_IN": 1809, "DIED_IN": 54, "RELEASED_IN": 6658},
    "year_1912": {"BORN_IN": 1856, "DIED_IN": 42, "RELEASED_IN": 5482},
    "year_1911": {"BORN_IN": 1754, "DIED_IN": 39, "RELEASED_IN": 4275},
    "year_1910": {"BORN_IN": 1782, "DIED_IN": 34, "RELEASED_IN": 3112},
    "year_1909": {"BORN_IN": 1742, "DIED_IN": 31, "RELEASED_IN": 1969},
    "year_1908": {"BORN_IN": 1780, "DIED_IN": 31, "RELEASED_IN": 1549},
    "year_1907": {"BORN_IN": 1701, "DIED_IN": 24, "RELEASED_IN": 1088},
    "year_1906": {"BORN_IN": 1602, "DIED_IN": 20, "RELEASED_IN": 940},
    "year_1905": {"BORN_IN": 1540, "DIED_IN": 24, "RELEASED_IN": 799},
    "year_1904": {"BORN_IN": 1625, "DIED_IN": 24, "RELEASED_IN": 992},
    "year_1903": {"BORN_IN": 1514, "DIED_IN": 22, "RELEASED_IN": 1840},
    "year_1902": {"BORN_IN": 1426, "DIED_IN": 16, "RELEASED_IN": 829},
    "year_1901": {"BORN_IN": 1458, "DIED_IN": 18, "RELEASED_IN": 1120},
    "year_1900": {"BORN_IN": 1321, "DIED_IN": 19, "RELEASED_IN": 1159},
    "year_1899": {"BORN_IN": 1293, "DIED_IN": 24, "RELEASED_IN": 1011},
    "year_1898": {"BORN_IN": 1282, "DIED_IN": 15, "RELEASED_IN": 916},
    "year_1897": {"BORN_IN": 1128, "DIED_IN": 13, "RELEASED_IN": 697},
    "year_1896": {"BORN_IN": 1166, "DIED_IN": 15, "RELEASED_IN": 568},
    "year_1895": {"BORN_IN": 1104, "DIED_IN": 18, "RELEASED_IN": 70},
    "year_1894": {"BORN_IN": 1073, "DIED_IN": 15, "RELEASED_IN": 46},
    "year_1893": {"BORN_IN": 1105, "DIED_IN": 14, "RELEASED_IN": 3},
    "year_1892": {"BORN_IN": 1113, "DIED_IN": 10, "RELEASED_IN": 8},
    "year_1891": {"BORN_IN": 1012, "DIED_IN": 13, "RELEASED_IN": 4},
    "year_1890": {"BORN_IN": 1010, "DIED_IN": 19, "RELEASED_IN": 2},
    "year_1889": {"BORN_IN": 1022, "DIED_IN": 21, "RELEASED_IN": 1},
    "year_1888": {"BORN_IN": 1021, "DIED_IN": 15, "RELEASED_IN": 4},
    "year_1887": {"BORN_IN": 886, "DIED_IN": 10, "RELEASED_IN": 15},
    "year_1886": {"BORN_IN": 861, "DIED_IN": 10, "RELEASED_IN": 0},
    "year_1885": {"BORN_IN": 840, "DIED_IN": 10, "RELEASED_IN": 1},
    "year_1884": {"BORN_IN": 801, "DIED_IN": 12, "RELEASED_IN": 0},
    "year_1883": {"BORN_IN": 707, "DIED_IN": 15, "RELEASED_IN": 1},
    "year_1882": {"BORN_IN": 705, "DIED_IN": 13, "RELEASED_IN": 0},
    "year_1881": {"BORN_IN": 629, "DIED_IN": 9, "RELEASED_IN": 1},
    "year_1880": {"BORN_IN": 648, "DIED_IN": 10, "RELEASED_IN": 0},
    "year_1879": {"BORN_IN": 611, "DIED_IN": 6, "RELEASED_IN": 0},
    "year_1878": {"BORN_IN": 572, "DIED_IN": 9, "RELEASED_IN": 2},
    "year_1877": {"BORN_IN": 489, "DIED_IN": 8, "RELEASED_IN": 0},
    "year_1876": {"BORN_IN": 501, "DIED_IN": 8, "RELEASED_IN": 0},
    "year_1875": {"BORN_IN": 479, "DIED_IN": 9, "RELEASED_IN": 0},
    "year_1874": {"BORN_IN": 458, "DIED_IN": 6, "RELEASED_IN": 1},
    "year_1873": {"BORN_IN": 401, "DIED_IN": 13, "RELEASED_IN": 0},
    "year_1872": {"BORN_IN": 390, "DIED_IN": 8, "RELEASED_IN": 0},
    "year_1871": {"BORN_IN": 343, "DIED_IN": 14, "RELEASED_IN": 0},
    "year_1870": {"BORN_IN": 371, "DIED_IN": 13, "RELEASED_IN": 371},
    "year_1869": {"BORN_IN": 326, "DIED_IN": 7, "RELEASED_IN": 326},
    "year_1868": {"BORN_IN": 268, "DIED_IN": 6, "RELEASED_IN": 268},
    "year_1867": {"BORN_IN": 286, "DIED_IN": 3, "RELEASED_IN": 286},
    "year_1866": {"BORN_IN": 269, "DIED_IN": 6, "RELEASED_IN": 269},
    "year_1865": {"BORN_IN": 252, "DIED_IN": 11, "RELEASED_IN": 252},
    "year_1864": {"BORN_IN": 212, "DIED_IN": 8, "RELEASED_IN": 212},
    "year_1863": {"BORN_IN": 235, "DIED_IN": 10, "RELEASED_IN": 235},
    "year_1862": {"BORN_IN": 212, "DIED_IN": 8, "RELEASED_IN": 212},
    "year_1861": {"BORN_IN": 166, "DIED_IN": 8, "RELEASED_IN": 166},
    "year_1860": {"BORN_IN": 194, "DIED_IN": 5, "RELEASED_IN": 194},
    "year_1859": {"BORN_IN": 149, "DIED_IN": 9, "RELEASED_IN": 149},
    "year_1858": {"BORN_IN": 150, "DIED_IN": 0, "RELEASED_IN": 150},
    "year_1857": {"BORN_IN": 131, "DIED_IN": 8, "RELEASED_IN": 131},
    "year_1856": {"BORN_IN": 93, "DIED_IN": 7, "RELEASED_IN": 93},
    "year_1855": {"BORN_IN": 92, "DIED_IN": 8, "RELEASED_IN": 92},
    "year_1854": {"BORN_IN": 97, "DIED_IN": 7, "RELEASED_IN": 97},
    "year_1853": {"BORN_IN": 91, "DIED_IN": 4, "RELEASED_IN": 91},
    "year_1852": {"BORN_IN": 76, "DIED_IN": 7, "RELEASED_IN": 76},
    "year_1851": {"BORN_IN": 74, "DIED_IN": 6, "RELEASED_IN": 74},
    "year_1850": {"BORN_IN": 68, "DIED_IN": 4, "RELEASED_IN": 68},
    "year_1849": {"BORN_IN": 51, "DIED_IN": 9, "RELEASED_IN": 51},
    "year_1848": {"BORN_IN": 61, "DIED_IN": 8, "RELEASED_IN": 61},
    "year_1847": {"BORN_IN": 45, "DIED_IN": 4, "RELEASED_IN": 45},
    "year_1846": {"BORN_IN": 47, "DIED_IN": 3, "RELEASED_IN": 47},
    "year_1845": {"BORN_IN": 28, "DIED_IN": 2, "RELEASED_IN": 28},
    "year_1844": {"BORN_IN": 35, "DIED_IN": 3, "RELEASED_IN": 35},
    "year_1843": {"BORN_IN": 22, "DIED_IN": 7, "RELEASED_IN": 22},
    "year_1842": {"BORN_IN": 42, "DIED_IN": 8, "RELEASED_IN": 42},
    "year_1841": {"BORN_IN": 26, "DIED_IN": 1, "RELEASED_IN": 26},
    "year_1840": {"BORN_IN": 21, "DIED_IN": 2, "RELEASED_IN": 21},
    "year_1839": {"BORN_IN": 26, "DIED_IN": 2, "RELEASED_IN": 26},
    "year_1838": {"BORN_IN": 22, "DIED_IN": 3, "RELEASED_IN": 22},
    "year_1837": {"BORN_IN": 20, "DIED_IN": 5, "RELEASED_IN": 20},
    "year_1836": {"BORN_IN": 22, "DIED_IN": 5, "RELEASED_IN": 22},
    "year_1835": {"BORN_IN": 18, "DIED_IN": 3, "RELEASED_IN": 18},
    "year_1834": {"BORN_IN": 18, "DIED_IN": 2, "RELEASED_IN": 18},
    "year_1833": {"BORN_IN": 12, "DIED_IN": 0, "RELEASED_IN": 12},
    "year_1832": {"BORN_IN": 14, "DIED_IN": 3, "RELEASED_IN": 14},
    "year_1831": {"BORN_IN": 15, "DIED_IN": 6, "RELEASED_IN": 15},
    "year_1830": {"BORN_IN": 20, "DIED_IN": 4, "RELEASED_IN": 20},
    "year_1829": {"BORN_IN": 15, "DIED_IN": 2, "RELEASED_IN": 15},
    "year_1828": {"BORN_IN": 17, "DIED_IN": 5, "RELEASED_IN": 17},
    "year_1827": {"BORN_IN": 10, "DIED_IN": 5, "RELEASED_IN": 10},
    "year_1826": {"BORN_IN": 9, "DIED_IN": 4, "RELEASED_IN": 9},
    "year_1825": {"BORN_IN": 13, "DIED_IN": 0, "RELEASED_IN": 13},
    "year_1824": {"BORN_IN": 13, "DIED_IN": 2, "RELEASED_IN": 13},
    "year_1823": {"BORN_IN": 11, "DIED_IN": 3, "RELEASED_IN": 11},
    "year_1822": {"BORN_IN": 14, "DIED_IN": 2, "RELEASED_IN": 14},
    "year_1821": {"BORN_IN": 20, "DIED_IN": 3, "RELEASED_IN": 20},
    "year_1820": {"BORN_IN": 11, "DIED_IN": 1, "RELEASED_IN": 11},
    "year_1819": {"BORN_IN": 15, "DIED_IN": 1, "RELEASED_IN": 15},
    "year_1818": {"BORN_IN": 8, "DIED_IN": 1, "RELEASED_IN": 8},
    "year_1817": {"BORN_IN": 10, "DIED_IN": 2, "RELEASED_IN": 10},
    "year_1816": {"BORN_IN": 7, "DIED_IN": 2, "RELEASED_IN": 7},
    "year_1815": {"BORN_IN": 8, "DIED_IN": 1, "RELEASED_IN": 8},
    "year_1814": {"BORN_IN": 10, "DIED_IN": 3, "RELEASED_IN": 10},
    "year_1813": {"BORN_IN": 15, "DIED_IN": 2, "RELEASED_IN": 15},
    "year_1812": {"BORN_IN": 12, "DIED_IN": 2, "RELEASED_IN": 12},
    "year_1811": {"BORN_IN": 15, "DIED_IN": 3, "RELEASED_IN": 15},
    "year_1810": {"BORN_IN": 16, "DIED_IN": 0, "RELEASED_IN": 16},
    "year_1809": {"BORN_IN": 13, "DIED_IN": 2, "RELEASED_IN": 13},
    "year_1808": {"BORN_IN": 9, "DIED_IN": 0, "RELEASED_IN": 9},
    "year_1807": {"BORN_IN": 6, "DIED_IN": 1, "RELEASED_IN": 6},
    "year_1806": {"BORN_IN": 8, "DIED_IN": 3, "RELEASED_IN": 8},
    "year_1805": {"BORN_IN": 7, "DIED_IN": 6, "RELEASED_IN": 7},
    "year_1804": {"BORN_IN": 14, "DIED_IN": 2, "RELEASED_IN": 14},
    "year_1803": {"BORN_IN": 10, "DIED_IN": 4, "RELEASED_IN": 10},
    "year_1802": {"BORN_IN": 8, "DIED_IN": 0, "RELEASED_IN": 8},
    "year_1801": {"BORN_IN": 9, "DIED_IN": 3, "RELEASED_IN": 9},
    "year_1800": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1799": {"BORN_IN": 7, "DIED_IN": 2, "RELEASED_IN": 7},
    "year_1798": {"BORN_IN": 6, "DIED_IN": 1, "RELEASED_IN": 6},
    "year_1797": {"BORN_IN": 11, "DIED_IN": 2, "RELEASED_IN": 11},
    "year_1796": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1795": {"BORN_IN": 5, "DIED_IN": 5, "RELEASED_IN": 5},
    "year_1794": {"BORN_IN": 1, "DIED_IN": 5, "RELEASED_IN": 1},
    "year_1793": {"BORN_IN": 5, "DIED_IN": 1, "RELEASED_IN": 5},
    "year_1792": {"BORN_IN": 7, "DIED_IN": 2, "RELEASED_IN": 7},
    "year_1791": {"BORN_IN": 9, "DIED_IN": 2, "RELEASED_IN": 9},
    "year_1790": {"BORN_IN": 5, "DIED_IN": 1, "RELEASED_IN": 5},
    "year_1789": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1788": {"BORN_IN": 5, "DIED_IN": 1, "RELEASED_IN": 5},
    "year_1787": {"BORN_IN": 1, "DIED_IN": 2, "RELEASED_IN": 1},
    "year_1786": {"BORN_IN": 5, "DIED_IN": 2, "RELEASED_IN": 5},
    "year_1785": {"BORN_IN": 4, "DIED_IN": 2, "RELEASED_IN": 4},
    "year_1784": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1783": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1782": {"BORN_IN": 5, "DIED_IN": 1, "RELEASED_IN": 5},
    "year_1781": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1780": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1779": {"BORN_IN": 3, "DIED_IN": 2, "RELEASED_IN": 3},
    "year_1778": {"BORN_IN": 3, "DIED_IN": 4, "RELEASED_IN": 3},
    "year_1777": {"BORN_IN": 4, "DIED_IN": 0, "RELEASED_IN": 4},
    "year_1776": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1775": {"BORN_IN": 5, "DIED_IN": 0, "RELEASED_IN": 5},
    "year_1774": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1773": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1772": {"BORN_IN": 4, "DIED_IN": 0, "RELEASED_IN": 4},
    "year_1771": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1770": {"BORN_IN": 5, "DIED_IN": 0, "RELEASED_IN": 5},
    "year_1769": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1768": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1767": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1766": {"BORN_IN": 4, "DIED_IN": 0, "RELEASED_IN": 4},
    "year_1765": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1764": {"BORN_IN": 2, "DIED_IN": 2, "RELEASED_IN": 2},
    "year_1763": {"BORN_IN": 1, "DIED_IN": 2, "RELEASED_IN": 1},
    "year_1761": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1760": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1759": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1758": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1757": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1756": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1755": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1754": {"BORN_IN": 2, "DIED_IN": 2, "RELEASED_IN": 2},
    "year_1751": {"BORN_IN": 4, "DIED_IN": 0, "RELEASED_IN": 4},
    "year_1750": {"BORN_IN": 1, "DIED_IN": 3, "RELEASED_IN": 1},
    "year_1749": {"BORN_IN": 5, "DIED_IN": 0, "RELEASED_IN": 5},
    "year_1748": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1747": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1746": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1745": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1744": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1743": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1741": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1740": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1739": {"BORN_IN": 1, "DIED_IN": 2, "RELEASED_IN": 1},
    "year_1737": {"BORN_IN": 4, "DIED_IN": 0, "RELEASED_IN": 4},
    "year_1736": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1735": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1734": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1733": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1732": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1731": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1730": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1729": {"BORN_IN": 1, "DIED_IN": 2, "RELEASED_IN": 1},
    "year_1728": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1727": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1726": {"BORN_IN": 1, "DIED_IN": 2, "RELEASED_IN": 1},
    "year_1725": {"BORN_IN": 4, "DIED_IN": 1, "RELEASED_IN": 4},
    "year_1724": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1723": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1722": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1720": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1718": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1717": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1716": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1715": {"BORN_IN": 1, "DIED_IN": 4, "RELEASED_IN": 1},
    "year_1714": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1713": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1712": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1711": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1710": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1707": {"BORN_IN": 3, "DIED_IN": 2, "RELEASED_IN": 3},
    "year_1706": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1703": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1701": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1700": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1699": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1698": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1697": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1696": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1695": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1694": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1693": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1689": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1688": {"BORN_IN": 2, "DIED_IN": 2, "RELEASED_IN": 2},
    "year_1686": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1685": {"BORN_IN": 5, "DIED_IN": 0, "RELEASED_IN": 5},
    "year_1684": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1681": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1679": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1678": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1677": {"BORN_IN": 1, "DIED_IN": 3, "RELEASED_IN": 1},
    "year_1676": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1674": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1673": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1672": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1671": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1670": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1669": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1668": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1667": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1664": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1660": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1659": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1658": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1657": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1656": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1655": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1654": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1653": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1652": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1651": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1648": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1646": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1645": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1644": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1643": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1641": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1640": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1639": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1638": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1637": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1636": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1635": {"BORN_IN": 1, "DIED_IN": 3, "RELEASED_IN": 1},
    "year_1634": {"BORN_IN": 1, "DIED_IN": 3, "RELEASED_IN": 1},
    "year_1633": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1632": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1631": {"BORN_IN": 1, "DIED_IN": 2, "RELEASED_IN": 1},
    "year_1630": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1629": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1628": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1627": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1626": {"BORN_IN": 1, "DIED_IN": 3, "RELEASED_IN": 1},
    "year_1625": {"BORN_IN": 0, "DIED_IN": 4, "RELEASED_IN": 0},
    "year_1623": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1622": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1621": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1619": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1618": {"BORN_IN": 1, "DIED_IN": 3, "RELEASED_IN": 1},
    "year_1616": {"BORN_IN": 1, "DIED_IN": 4, "RELEASED_IN": 1},
    "year_1614": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1613": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1611": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1610": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1609": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1608": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1606": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1604": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1602": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1601": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1600": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1599": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1595": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1594": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1593": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1592": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1591": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1589": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1587": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1586": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1585": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1584": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1583": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1581": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1580": {"BORN_IN": 3, "DIED_IN": 2, "RELEASED_IN": 3},
    "year_1579": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1578": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1577": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1576": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1574": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1572": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1571": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1569": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1568": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1567": {"BORN_IN": 3, "DIED_IN": 1, "RELEASED_IN": 3},
    "year_1566": {"BORN_IN": 1, "DIED_IN": 3, "RELEASED_IN": 1},
    "year_1564": {"BORN_IN": 2, "DIED_IN": 1, "RELEASED_IN": 2},
    "year_1563": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1562": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1561": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1560": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1558": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1556": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1553": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_1550": {"BORN_IN": 3, "DIED_IN": 0, "RELEASED_IN": 3},
    "year_1549": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1547": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1544": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1543": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1542": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1541": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1540": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1533": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1532": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1530": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1529": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1527": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1525": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1524": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1521": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1519": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1511": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1510": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1508": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1506": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1505": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1504": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1503": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1494": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1493": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1492": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1485": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1479": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1475": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1474": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1473": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1471": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1470": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1469": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1468": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1465": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1463": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1452": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1448": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1440": {"BORN_IN": 2, "DIED_IN": 0, "RELEASED_IN": 2},
    "year_1431": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_1422": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1420": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1414": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1413": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1412": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1408": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1400": {"BORN_IN": 0, "DIED_IN": 3, "RELEASED_IN": 0},
    "year_1398": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1375": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1361": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1350": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1343": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1335": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1330": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1321": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1313": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1291": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1283": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1273": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1265": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1250": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1220": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1207": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1191": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1180": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1179": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1155": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_1150": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1130": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1098": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1095": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1067": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_1031": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_973": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_840": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_770": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_485": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_235": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_165": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_163": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_140": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_122": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_95": {"BORN_IN": 1, "DIED_IN": 1, "RELEASED_IN": 1},
    "year_69": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_66": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_65": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_59": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_46": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_37": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_27": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_21": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_17": {"BORN_IN": 0, "DIED_IN": 2, "RELEASED_IN": 0},
    "year_6": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_5": {"BORN_IN": 0, "DIED_IN": 1, "RELEASED_IN": 0},
    "year_4": {"BORN_IN": 1, "DIED_IN": 0, "RELEASED_IN": 1},
    "year_0": {"BORN_IN": 3209521, "DIED_IN": 3453973, "RELEASED_IN": 624693},
}
incoming_rel_counts.update(year_incoming_rel_counts)

import re
import csv

def format_number(num):
    try:
        return f"{int(num):,}"
    except (ValueError, TypeError):
        return num

def get_node_count(lbl):
    """Fungsi pencari agar kode lebih bersih saat mencari jumlah node"""
    if lbl in person_node_counts: return person_node_counts[lbl]
    if lbl in movie_node_counts: return movie_node_counts[lbl]
    if lbl in category_label_counts: return category_label_counts[lbl]
    if lbl in year_label_counts: return year_label_counts[lbl]
    return "xxxxxx"

def transform_query(query):
    # --- 1. MENGUBAH SISA PROPERTI DI KLAUSA WHERE ---
    def property_replacer(match):
        # Karena properti sekarang nyaris hanya '.name', kita biarkan persis aslinya
        return match.group(0)

    # Menangkap properti yang tersisa di WHERE (seperti n1.name="Kim Angeli")
    prop_pattern = re.compile(r'(?P<var>\w+)\.(?P<prop>\w+)\s*=\s*(?P<val>"[^"]*"|\'[^\']*\'|[0-9]+)')
    query = prop_pattern.sub(property_replacer, query)

    # --- 2. MENGUBAH ALUR RELASI (CHAINING MULTI-HOP) ---
    def chain_replacer(match):
        s_var = match.group('s_var')
        s_lbl = match.group('s_lbl')
        r_lbl = match.group('r_lbl')
        t_lbl = match.group('t_lbl') # Diambil dari intipan (lookahead)

        s_count = get_node_count(s_lbl)
        out_count = outgoing_rel_counts.get(s_lbl, {}).get(r_lbl, "xxxxxx")
        in_count = incoming_rel_counts.get(t_lbl, {}).get(r_lbl, "xxxxxx")

        # Node asal dan relasi di-replace, tapi node target (t_lbl) TIDAK DISENTUH
        return f"({s_var}:{format_number(s_count)}) -[{format_number(out_count)}]-[{format_number(in_count)}]-> "

    # REGEX MULTI-HOP: (NodeAsal)-[Relasi]->(?=IntipNodeTarget)
    # Trik lookahead (?=...) akan menjaga Node Target tetap utuh untuk dilooping di hop berikutnya
    path_pattern = re.compile(
        r'\((?P<s_var>\w*):(?P<s_lbl>[a-zA-Z]\w*)\)\s*-\[\s*(?:\w*\s*:)?\s*(?P<r_lbl>\w+)\s*\]->\s*(?=\((?P<t_var>\w*):(?P<t_lbl>[a-zA-Z]\w*)\))'
    )
    query = path_pattern.sub(chain_replacer, query)

    # --- 3. MENGUBAH SISA NODE TARGET TERAKHIR ---
    def node_replacer(match):
        var = match.group('var')
        lbl = match.group('lbl')
        count = get_node_count(lbl)
        var_str = f"{var}:" if var else ":"
        return f"({var_str}{format_number(count)})"

    # Karena step 2 menjaga target terakhir tetap utuh, regex ini akan mengubah 
    # node-node yang tertinggal di ujung kueri (seperti (:year_1993) atau (n1:adventure))
    node_pattern = re.compile(r'\((?P<var>\w*):(?P<lbl>[a-zA-Z]\w*)\)')
    query = node_pattern.sub(node_replacer, query)

    return query

def cari_filter_pertama_pbn(query):
    path_pattern = re.compile(
        r'\((?P<s_var>\w*):(?P<s_lbl>[a-zA-Z]\w*)\)\s*-\[\s*(?:\w*\s*:)?\s*(?P<r_lbl>\w+)\s*\]->\s*(?=\((?P<t_var>\w*):(?P<t_lbl>[a-zA-Z]\w*)\))'
    )

    kandidat = []  # list of (nilai, var, label)

    for m in path_pattern.finditer(query):
        s_var, s_lbl = m.group('s_var'), m.group('s_lbl')
        r_lbl = m.group('r_lbl')
        t_var, t_lbl = m.group('t_var'), m.group('t_lbl')

        s_count = get_node_count(s_lbl)
        t_count = get_node_count(t_lbl)
        out_count = outgoing_rel_counts.get(s_lbl, {}).get(r_lbl)
        in_count = incoming_rel_counts.get(t_lbl, {}).get(r_lbl)

        if isinstance(s_count, int):
            kandidat.append((s_count, s_var, s_lbl))
        if isinstance(t_count, int):
            kandidat.append((t_count, t_var, t_lbl))
        if isinstance(out_count, int):
            kandidat.append((out_count, s_var, s_lbl))
        if isinstance(in_count, int):
            kandidat.append((in_count, t_var, t_lbl))

    if not kandidat:
        return "-"

    nilai_min, var_min, lbl_min = min(kandidat, key=lambda x: x[0])

    # Node anonim (tanpa variabel, misal hasil refaktorisasi seperti (:year_1973))
    if var_min:
        return f"{var_min}:{lbl_min}"
    else:
        return f":{lbl_min}"

# ==============================================================
# FUNGSI EXPORT CSV (Tetap sama seperti sebelumnya)
# ==============================================================
def transform_file_kueri_pbn_to_numeric(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            daftar_kueri_asli = [line.strip() for line in f.readlines() if line.strip()]

        print(f"Berhasil membaca {len(daftar_kueri_asli)} kueri dari {input_file}...")

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(['kueri asal', 'kueri numerik', 'filter pertama'])

            for kueri_asli in daftar_kueri_asli:
                kueri_numerik = transform_query(kueri_asli)
                filter_pertama = cari_filter_pertama_pbn(kueri_asli)
                writer.writerow([kueri_asli, kueri_numerik, filter_pertama])

        print(f"Selesai! Hasil telah disimpan ke dalam {output_file}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# # ==============================================================
# # EKSEKUSI PROGRAM
# # ==============================================================
# nama_file_input = 'Query_Where_80_Refactored.txt'
# nama_file_output = 'Refactored_Query_PBN_Numerik.csv'

# proses_file_kueri(nama_file_input, nama_file_output)