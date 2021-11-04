package org.edgegallery.locservice.manager.data;

public class Map1 extends Map
{
    private static final int INIT_X = 10;
    private static final int FIXED_Y = 200;
    private static final int STEP_LEN = 10;
    public Map1(int mapId, float maxX, float maxY, float maxZ) {
        super(mapId, maxX, maxY, maxZ);
    }

    @Override
    public void init(Location location, Location initLoc) {
        location.setX(INIT_X);
        location.setY(FIXED_Y);
        location.setZ(0);

        // location.setGoMode(1);
    }

    @Override
    public void goStep(Location location) {
        if (location.getX() + STEP_LEN <= getMaxX()) {
            location.setX(location.getX() + STEP_LEN);
        } else {
            location.setX(getMaxX());
        }
        // if (location.getGoMode() == 1) {
        //     if (location.getX() + STEP_LEN <= getMaxX()) {
        //         location.setX(location.getX() + STEP_LEN);
        //     } else {
        //         location.setX(getMaxX());
        //         location.setGoMode(2);
        //     }
        // } else {
        //     if (location.getX() - STEP_LEN >= INIT_X) {
        //         location.setX(location.getX() - STEP_LEN);
        //     } else {
        //         location.setX(INIT_X);
        //         location.setGoMode(1);
        //     }
        // }
    }
}
