# 前端

1、frontend编译生成static

npm install

npm run build


2、website-gateway-locapp编译

拷贝static目录到website-gateway-locapp/src/main/resources目录

mvn clean install

把target/website-gateway-locapp-1.0.0.jar拷贝到frontend

# LocationService

cd ./location-service

mvn clean install

把target/location-service.jar拷贝到location-service

# 依赖

linux版本的jre，重命名为jre.tar.gz放到3rd目录。

根据jre包里面的目录名称，调整install.sh和start.sh中的JRE_DIR

# 打包

进入build目录

执行build.sh脚本完成打包，生成location-app-1.0.tar
