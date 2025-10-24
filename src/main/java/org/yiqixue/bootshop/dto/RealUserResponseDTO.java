package org.yiqixue.bootshop.dto;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.time.LocalDate;

/**
 * 用户响应DTO - 返回给前端的数据
 * ✅ 不包含敏感信息（如密码）
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder

public class RealUserResponseDTO {

    private Long id;
    private String username;
    private String email;
    private String phone;
    private String realName;
    private String gender;
    private LocalDate birthDate;
    private Integer age;
    private String country;
    private String city;
    private String bio;
    private String hobbies;
    private Boolean newsletterSubscription;
    private LocalDate registerDate;


    // 注意：没有password字段！
}
