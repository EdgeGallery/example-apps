package org.edgegallery.locservice.manager.data;

public class Map2 extends Map
{
    private static final int INIT_X = 650;
    private static final int INIT_Y = 720;
    public Map2(int mapId, float maxX, float maxY, float maxZ) {
        super(mapId, maxX, maxY, maxZ);
    }

    @Override
    public void init(Location location, Location initLoc) {
        location.setX(INIT_X);
        location.setY(INIT_Y);
        location.setZ(0);

        location.setGoMode(1);
    }

    @Override
    public void goStep(Location location) {
        switch (location.getGoMode()) {
            case 1: {
                location.setX(location.getX() + 20);
                location.setY(location.getY() - 4);
                if (location.getX() >= 925) {
                    location.setGoMode(2);
                }
                break;
            }
            case 2: {
                if (location.getX() < 1290) {
                    location.setX(location.getX() + 30);
                } else {
                    Map thirdMap = new Map3(3, 1200, 1000, 100);
                    location.setMap(thirdMap);
                    thirdMap.init(location, null);
                }
                break;
            }
            default: {
                break;
            }
        }
    }
}
