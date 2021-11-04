/*
 *  Copyright 2021 Huawei Technologies Co., Ltd.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

package org.edgegallery.locservice.manager;

import org.edgegallery.locservice.manager.data.Location;
import org.edgegallery.locservice.manager.data.Map5;
import org.edgegallery.locservice.manager.data.Map6;
import org.edgegallery.locservice.manager.data.Map7;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class LocationManager {

    private static final Logger LOGGER = LoggerFactory.getLogger(LocationManager.class);

    private static final String FIXED_UEID = "imsi:999999999999999";

    private static final Object LOCK_OBJ = new Object();

    private static LocationManager locationManager = null;

    private Location currLoc = null;

    private LocationManager() {}

    public static LocationManager getInstance() {
        if (locationManager != null) {
            return locationManager;
        }

        synchronized (LOCK_OBJ) {
            if (locationManager == null) {
                locationManager = new LocationManager();
                locationManager.initLocationData();
            }
        }
        return locationManager;
    }

    private void initLocationData() {
        currLoc = new Location();
        // currLoc.init(FIXED_UEID, new FirstMap(1, 2000, 1000, 100));
        currLoc.init(FIXED_UEID, new Map5(5, 1920, 1080, 100));
        // currLoc.init(FIXED_UEID, new Map6(6, 1200, 1000, 100));

        LocationChangeTask locationChangeTask = new LocationChangeTask(currLoc);
        Thread locationChangeThread = new Thread(locationChangeTask);
        locationChangeThread.setName("LocationChangeTask");
        locationChangeThread.start();
    }

    public Location getCurrLocation(String ueId) {
        return currLoc;
    }
}

class LocationChangeTask implements Runnable {
    private static final Logger LOGGER = LoggerFactory.getLogger(LocationChangeTask.class);
    private Location currLoc = null;

    public LocationChangeTask(Location currLoc) {
        this.currLoc = currLoc;
    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(1200);
            } catch (InterruptedException e) {
                LOGGER.error("sleep exception");
            }

            currLoc.goStep();
        }
    }
}
