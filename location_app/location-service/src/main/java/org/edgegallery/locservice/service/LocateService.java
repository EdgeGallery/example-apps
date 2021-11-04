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

package org.edgegallery.locservice.service;

import fj.data.Either;
import org.edgegallery.locservice.controller.dto.response.FormatRespDto;
import org.edgegallery.locservice.controller.dto.response.GetHelperLocationRespDto;
import org.edgegallery.locservice.controller.dto.response.GetLocationRespDto;
import org.edgegallery.locservice.controller.dto.response.HelperLocationInfo;
import org.edgegallery.locservice.controller.dto.response.LocationInfo;
import org.edgegallery.locservice.manager.LocationManager;
import org.edgegallery.locservice.manager.data.Location;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service("locateService")
public class LocateService {

    private static final Logger LOGGER = LoggerFactory.getLogger(LocateService.class);

    public Either<GetLocationRespDto, FormatRespDto> getLocation(String ueId) {
        LOGGER.info("get location info, ueId = {}", ueId);
        Location currLoc = LocationManager.getInstance().getCurrLocation(ueId);

        GetLocationRespDto getLocationRespDto = new GetLocationRespDto();
        getLocationRespDto.setUeId(ueId);
        getLocationRespDto.setTimestamp(System.currentTimeMillis());

        LocationInfo locationInfo = new LocationInfo();
        locationInfo.assign(currLoc);
        getLocationRespDto.setLocationInfo(locationInfo);

        LOGGER.info("get location info succeed, ueId = {}", ueId);
        return Either.left(getLocationRespDto);
    }

    public Either<GetHelperLocationRespDto, FormatRespDto> getHelperLocation(String ueId) {
        LOGGER.info("get location info, ueId = {}", ueId);
        Location currLoc = LocationManager.getInstance().getCurrLocation(ueId);

        GetHelperLocationRespDto getLocationRespDto = new GetHelperLocationRespDto();
        getLocationRespDto.setUeId(ueId);
        getLocationRespDto.setTimestamp(System.currentTimeMillis());

        HelperLocationInfo locationInfo = new HelperLocationInfo();
        locationInfo.assign(currLoc);
        getLocationRespDto.setLocationInfo(locationInfo);

        LOGGER.info("get location info succeed, ueId = {}", ueId);
        return Either.left(getLocationRespDto);
    }
}
