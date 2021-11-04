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

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import org.edgegallery.locservice.manager.data.Map;
import org.edgegallery.locservice.manager.data.Map2;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public final class MapManager {

    private static final Logger LOGGER = LoggerFactory.getLogger(MapManager.class);

    private static final Object LOCK_OBJ = new Object();

    private static final Random RANDOM_INSTANCE = new Random();

    private static MapManager mapManager = null;

    private List<Map> mapList = new ArrayList<>();

    private MapManager() {}

    public static MapManager getInstance() {
        if (mapManager != null) {
            return mapManager;
        }

        synchronized (LOCK_OBJ) {
            if (mapManager == null) {
                mapManager = new MapManager();
                mapManager.loadMap();
            }
        }
        return mapManager;
    }

    private void loadMap() {
        // mapList.add(new FirstMap(1, 2000, 1000, 100));
        mapList.add(new Map2(2, 1200, 1000, 100));
    }

    public Map randomMap() {
        return mapList.get(RANDOM_INSTANCE.nextInt(mapList.size()));
    }
}
