package org.edgegallery.locservice.manager.data;

public class Map6 extends Map
{
    private static final int INIT_X = 1300;
    private static final int INIT_Y = 90;
    public Map6(int mapId, float maxX, float maxY, float maxZ) {
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
        location.setHeader("header_6_1");
    }

    @Override
    public void goStep(Location location) {
        switch (location.getGoMode()) {
            case 1: {
                location.setHide(false);
                location.setHeader("header_6_1");
                location.setHx(location.getHx() - 80);
                location.setHy(location.getHy() + 36);
                if (location.getHx() <= 580) {
                    location.setGoMode(2);
                }
                break;
            }
            case 2: {
                location.setHide(true);
                location.setHx(location.getHx() - 80);
                location.setHy(location.getHy() + 36);
                if (location.getHx() <= 420) {
                    location.setGoMode(3);
                }
                break;
            }
            case 3: {
                location.setHide(true);
                location.setHx(location.getHx() + 80);
                location.setHy(location.getHy() + 36);
                if (location.getHx() >= 1380) {
                    Map map5 = new Map5(5, 0, 0, 0);
                    location.setMap(map5);

                    Location initLoc = new Location();
                    initLoc.setHx(530);
                    initLoc.setHy(550);
                    initLoc.setHz(0);
                    initLoc.setGoMode(11);
                    initLoc.setHide(false);
                    initLoc.setHeader("header_5_2");
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
