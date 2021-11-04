package org.edgegallery.locservice.manager.data;

public class Map7 extends Map
{
    private static final int INIT_X = 80;
    private static final int INIT_Y = 540;
    public Map7(int mapId, float maxX, float maxY, float maxZ) {
        super(mapId, maxX, maxY, maxZ);
    }

    @Override
    public void init(Location location, Location initLoc) {
        location.setHx(INIT_X);
        location.setHy(INIT_Y);
        location.setHz(0);

        location.setX(location.getHx());
        location.setY(location.getHy());
        location.setZ(location.getHz());

        location.setGoMode(1);
        location.setHide(false);
        location.setHeader("header_7_2");
    }

    @Override
    public void goStep(Location location) {
        switch (location.getGoMode()) {
            case 1: {
                location.setHide(false);
                location.setHeader("header_7_2");
                location.setHx(location.getHx() + 80);
                location.setHy(location.getHy() + 36);
                if (location.getHx() >= 540) {
                    location.setGoMode(2);
                }
                break;
            }
            case 2: {
                location.setHide(true);
                location.setHx(location.getHx() + 80);
                location.setHy(location.getHy() + 36);
                if (location.getHx() >= 620) {
                    location.setGoMode(3);
                }
                break;
            }
            case 3: {
                location.setHide(true);
                location.setHx(location.getHx() + 80);
                location.setHy(location.getHy() - 36);
                if (location.getHx() >= 1340) {
                    location.setGoMode(4);
                }
                break;
            }
            case 4: {
                location.setHide(true);
                location.setHx(location.getHx() + 80);
                location.setHy(location.getHy() - 36);
                if (location.getHx() >= 1740) {
                    location.setGoMode(5);
                }
                break;
            }
            case 5: {
                location.setHide(true);
                location.setHx(location.getHx() + 40);
                location.setHy(location.getHy() - 18);
                if (location.getHx() >= 1780) {
                    location.setGoMode(6);
                }
                break;
            }
            case 6: {
                location.setHide(false);
                location.setHeader("header_7_4");
                location.setHx(location.getHx() - 80);
                location.setHy(location.getHy() - 32);
                if (location.getHx() <= 1260) {
                    Map map5 = new Map5(5, 0, 0, 0);
                    location.setMap(map5);

                    Location initLoc = new Location();
                    initLoc.setHx(1460);
                    initLoc.setHy(380);
                    initLoc.setHz(0);
                    initLoc.setGoMode(21);
                    initLoc.setHide(false);
                    initLoc.setHeader("header_5_4");
                    map5.init(location, initLoc);
                }
                break;
            }
            default: {
                break;
            }
        }

        location.setX(location.getHx());
        location.setY(location.getHy());
        location.setZ(location.getHz());
    }
}
