package org.yiqixue.bootshop.dto;

import jakarta.validation.constraints.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.time.LocalDate;


/**
 * 用户更新DTO - 用于更新用户信息
 * 注意：更新和注册的验证规则可能不同
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class RealUserUpdateDTO {

    @NotNull(message = "用户ID不能为空")
    private Integer id;

    // 更新时不需要验证用户名（不允许修改）
    // private String username;

    // 更新时密码是可选的
    @Size(min = 6, message = "密码长度不能少于6个字符")
    private String password;

    @Email(message = "邮箱格式不正确")
    private String email;

    @Pattern(regexp = "^1[3-9]\\d{9}$", message = "请输入正确的手机号码")
    private String phone;

    private String realName;
    private String gender;
    private LocalDate birthDate;

    @Min(value = 18, message = "年龄必须大于等于18岁")
    @Max(value = 120, message = "年龄不能超过120岁")
    private Integer age;

    private String country;
    private String city;
    private String bio;
    private String hobbies;
    private Boolean newsletterSubscription;
}
