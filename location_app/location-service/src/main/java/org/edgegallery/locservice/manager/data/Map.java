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

package org.edgegallery.locservice.manager.data;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.edgegallery.locservice.manager.data.Location;

@ToString
@Setter
@Getter
@AllArgsConstructor
public abstract class Map {
    protected static final long TARGET_POINT_WAITTIME = 3000;

    protected static final long START_POINT_WAITTIME = 5000;

    private int mapId;

    private float maxX;

    private float maxY;

    private float maxZ;

    abstract public void init(Location location, Location initLoc);

    abstract public void goStep(Location location);
}
