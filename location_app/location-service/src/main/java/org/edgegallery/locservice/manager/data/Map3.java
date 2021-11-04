package org.edgegallery.locservice.manager.data;

public class Map3 extends Map
{
    private static final int INIT_X = 1600;
    private static final int INIT_Y = 700;
    public Map3(int mapId, float maxX, float maxY, float maxZ) {
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
                location.setX(location.getX() - 100);
                location.setY(location.getY() - 90);
                if (location.getX() <= 1400) {
                    location.setGoMode(2);
                }
                break;
            }
            case 2: {
                location.setX(location.getX() - 150);
                location.setY(location.getY() - 2);
                if (location.getX() <= 1150) {
                    location.setGoMode(3);
                }
                break;
            }
            case 3: {
                location.setX(location.getX() - 100);
                location.setY(location.getY() - 80);
                if (location.getX() <= 700) {
                    location.setGoMode(4);
                }
                break;
            }
            case 4: {
                if (location.getX() < 800) {
                    location.setX(location.getX() + 50);
                } else {
                    Map fourthMap = new Map4(4, 1200, 1000, 100);
                    location.setMap(fourthMap);
                    fourthMap.init(location, null);
                }
                break;
            }
            default: {
                break;
            }
        }
    }
}
