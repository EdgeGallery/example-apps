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

package org.edgegallery.locservice.controller.dto.response;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.edgegallery.locservice.manager.data.Location;

@ToString
@Setter
@Getter
public class HelperLocationInfo {

    private int mapId;

    private float x;

    private float y;

    private float z;

    private float hx;

    private float hy;

    private float hz;

    private boolean hide = false;

    private String header;

    public void assign(Location currLoc) {
        setMapId(currLoc.getMap().getMapId());
        setX(currLoc.getX());
        setY(currLoc.getY());
        setZ(currLoc.getZ());

        setHx(currLoc.getHx());
        setHy(currLoc.getHy());
        setHz(currLoc.getHz());

        setHide(currLoc.isHide());
        setHeader(currLoc.getHeader());
    }
}
