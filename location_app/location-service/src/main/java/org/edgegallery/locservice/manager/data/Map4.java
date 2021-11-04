package org.edgegallery.locservice.manager.data;

public class Map4 extends Map
{
    private static final int INIT_X = 1880;
    private static final int INIT_Y = 600;
    public Map4(int mapId, float maxX, float maxY, float maxZ) {
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
                location.setX(location.getX() - 200);
                location.setY(location.getY() - 2);
                if (location.getX() <= 1360) {
                    location.setGoMode(2);
                }
                break;
            }
            case 2: {
                if (location.getX() <= 1550) {
                    location.setX(location.getX() + 80);
                    location.setY(location.getY() - 16);
                } else {
                    Map secondMap = new Map2(2, 1200, 1000, 100);
                    location.setMap(secondMap);
                    secondMap.init(location, null);
                }
                break;
            }
            default: {
                break;
            }
        }
    }
}
