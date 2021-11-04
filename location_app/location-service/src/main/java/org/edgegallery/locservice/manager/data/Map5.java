package org.edgegallery.locservice.manager.data;

public class Map5 extends Map
{
    private static final int INIT_X = 900;
    private static final int INIT_Y = 155;
    private static final int UPSTAIR_Y = 432;
    public Map5(int mapId, float maxX, float maxY, float maxZ) {
        super(mapId, maxX, maxY, maxZ);
    }

    @Override
    public void init(Location location, Location initLoc) {
        if (initLoc == null) {
            location.setHx(INIT_X);
            location.setHy(INIT_Y);
            location.setHz(0);


            location.setGoMode(1);
            location.setHide(false);
            location.setHeader("header_5_1");
        } else {
            location.setHx(initLoc.getHx());
            location.setHy(initLoc.getHy());
            location.setHz(initLoc.getHz());

            location.setGoMode(initLoc.getGoMode());
            location.setHide(initLoc.isHide());
            location.setHeader(initLoc.getHeader());
        }

        location.setX(location.getHx());
        location.setY(location.getHy());
        location.setZ(location.getHz());
    }

    @Override
    public void goStep(Location location) {
        boolean flag = true;
        switch (location.getGoMode()) {
            case 1: {
                location.setHide(false);
                location.setHeader("header_5_1");
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() <= 820) {
                    location.setGoMode(2);
                }
                break;
            }
            case 2: {
                location.setHide(true);
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() <= 760) {
                    location.setGoMode(3);
                }
                break;
            }
            case 3: {
                location.setHide(false);
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() <= 640) {
                    location.setGoMode(4);
                }
                break;
            }
            case 4: {
                location.setHide(true);
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() <= 520) {
                    Map map6 = new Map6(6, 0, 0, 0);
                    location.setMap(map6);
                    map6.init(location, null);
                }
                break;
            }
            case 11: {
                location.setHide(false);
                location.setHeader("header_5_2");
                location.setHx(location.getHx() + 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() >= 570) {
                    location.setGoMode(12);
                }
                break;
            }
            case 12: {
                location.setHide(false);
                location.setHeader("header_5_3");
                location.setHx(location.getHx() + 20);
                location.setHy(location.getHy() - 8);
                if (location.getHx() >= 780) {
                    location.setGoMode(13);
                }
                break;
            }
            case 13: {
                location.setHide(true);
                location.setHx(location.getHx() + 20);
                location.setHy(location.getHy() - 8);
                if (location.getHx() >= 900) {
                    location.setGoMode(14);
                }
                break;
            }
            case 14: {
                flag = false;
                location.setHide(true);
                location.setHx(location.getHx());
                location.setHy(location.getHy() - 10);

                location.setX(location.getHx());
                location.setY(UPSTAIR_Y);
                location.setZ(location.getZ() + 10);
                if (location.getHy() <= 232) {
                    location.setGoMode(15);
                    location.setTime(System.currentTimeMillis());
                }
                break;
            }
            case 15: {
                flag = false;
                location.setHide(true);
                if (System.currentTimeMillis() - location.getTime() >= TARGET_POINT_WAITTIME) {
                    location.setGoMode(16);
                }
                break;
            }
            case 16: {
                flag = false;
                location.setHide(true);
                location.setHx(location.getHx());
                location.setHy(location.getHy() + 10);

                location.setX(location.getHx());
                location.setY(UPSTAIR_Y);
                location.setZ(location.getZ() - 10);
                if (location.getHy() >= UPSTAIR_Y) {
                    location.setGoMode(17);
                }
                break;
            }
            case 17: {
                location.setHide(true);
                location.setHx(location.getHx() + 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() >= 960) {
                    location.setGoMode(18);
                }
                break;
            }
            case 18: {
                location.setHide(false);
                location.setHeader("header_5_2");
                location.setHx(location.getHx() + 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() >= 1000) {
                    location.setGoMode(19);
                }
                break;
            }
            case 19: {
                location.setHide(true);
                location.setHx(location.getHx() + 20);
                location.setHy(location.getHy() + 9);
                if (location.getHx() >= 1160) {
                    Map map7 = new Map7(7, 0, 0, 0);
                    location.setMap(map7);
                    map7.init(location, null);
                }
                break;
            }
            case 21: {
                location.setHide(false);
                location.setHeader("header_5_4");
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() - 8);
                if (location.getHx() <= 1420) {
                    location.setGoMode(22);
                }
                break;
            }
            case 22: {
                location.setHide(true);
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() - 8);
                if (location.getHx() <= 1340) {
                    location.setGoMode(23);
                }
                break;
            }
            case 23: {
                location.setHide(false);
                location.setHeader("header_5_4");
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() - 8);
                if (location.getHx() <= 1280) {
                    location.setGoMode(24);
                }
                break;
            }
            case 24: {
                location.setHide(true);
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() - 8);
                if (location.getHx() <= 1020) {
                    location.setGoMode(25);
                }
                break;
            }
            case 25: {
                location.setHide(false);
                location.setHeader("header_5_4");
                location.setHx(location.getHx() - 20);
                location.setHy(location.getHy() - 8);
                if (location.getHx() <= INIT_X) {
                    location.setGoMode(26);
                    location.setTime(System.currentTimeMillis());
                }
                break;
            }
            case 26: {
                location.setHide(false);
                location.setHeader("header_5_4");
                if (System.currentTimeMillis() - location.getTime() >= START_POINT_WAITTIME) {
                    location.setGoMode(1);
                    init(location, null);
                }
                break;
            }
            default: {
                break;
            }
        }

        if (flag) {
            location.setX(location.getHx());
            location.setY(location.getHy());
            location.setZ(0);
        }
    }
}
