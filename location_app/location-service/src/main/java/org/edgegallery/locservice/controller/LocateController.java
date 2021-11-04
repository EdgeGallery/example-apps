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

package org.edgegallery.locservice.controller;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import javax.servlet.http.HttpServletRequest;
import javax.ws.rs.core.Response;
import org.apache.http.HttpStatus;
import org.edgegallery.locservice.controller.base.BeGenericServlet;
import org.edgegallery.locservice.controller.dto.response.ErrorRespDto;
import org.edgegallery.locservice.controller.dto.response.FormatRespDto;
import org.edgegallery.locservice.controller.dto.response.GetHelperLocationRespDto;
import org.edgegallery.locservice.controller.dto.response.GetLocationRespDto;
import org.edgegallery.locservice.service.LocateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/location/v1")
@Controller
public class LocateController extends BeGenericServlet {

    @Autowired
    private LocateService locService;

    @GetMapping(value = "/users", produces = MediaType.APPLICATION_JSON_VALUE)
    @ApiOperation(value = "get current location", response = Object.class)
    @ApiResponses(value = {
        @ApiResponse(code = HttpStatus.SC_OK, message = "register success", response = GetLocationRespDto.class),
        @ApiResponse(code = HttpStatus.SC_BAD_REQUEST, message = "Bad Request", response = ErrorRespDto.class),
        @ApiResponse(code = HttpStatus.SC_INTERNAL_SERVER_ERROR, message = "INTERNAL ERROR",
            response = ErrorRespDto.class)
    })
    public ResponseEntity<Object> getLocation(HttpServletRequest httpRequest) {
        String ueId = httpRequest.getParameter("address");
        if (StringUtils.isEmpty(ueId)) {
            FormatRespDto formatRespDto = new FormatRespDto(Response.Status.BAD_REQUEST,
                "wrong ueid parameter.");
            return ResponseEntity.status(formatRespDto.getErrStatus().getStatusCode())
                .body(formatRespDto.getErrorRespDto());
        }
        return buildCreatedResponse(locService.getLocation(ueId));
    }

    @GetMapping(value = "/user", produces = MediaType.APPLICATION_JSON_VALUE)
    @ApiOperation(value = "get current location with helper info", response = Object.class)
    @ApiResponses(value = {
        @ApiResponse(code = HttpStatus.SC_OK, message = "register success", response = GetHelperLocationRespDto.class),
        @ApiResponse(code = HttpStatus.SC_BAD_REQUEST, message = "Bad Request", response = ErrorRespDto.class),
        @ApiResponse(code = HttpStatus.SC_INTERNAL_SERVER_ERROR, message = "INTERNAL ERROR",
            response = ErrorRespDto.class)
    })
    public ResponseEntity<Object> getHelperLocation(HttpServletRequest httpRequest) {
        String ueId = httpRequest.getParameter("address");
        if (StringUtils.isEmpty(ueId)) {
            FormatRespDto formatRespDto = new FormatRespDto(Response.Status.BAD_REQUEST,
                "wrong ueid parameter.");
            return ResponseEntity.status(formatRespDto.getErrStatus().getStatusCode())
                .body(formatRespDto.getErrorRespDto());
        }
        return buildCreatedResponse(locService.getHelperLocation(ueId));
    }
}
