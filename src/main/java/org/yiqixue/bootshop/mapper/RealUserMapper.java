package org.yiqixue.bootshop.mapper;

import org.yiqixue.bootshop.dto.*;
import org.yiqixue.bootshop.dto.RealUserRegistrationDTO;
import org.yiqixue.bootshop.dto.RealUserRegistrationDTO;
import org.yiqixue.bootshop.entity.RealUser;
import org.springframework.stereotype.Component;

/**
 * 用户映射器 - 负责DTO和Entity之间的转换
 * 生产环境推荐使用 MapStruct 自动生成映射代码
 */
@Component
public class RealUserMapper {

    /**
     * 注册DTO转Entity
     */
    public RealUser toEntity(RealUserRegistrationDTO dto) {
        return RealUser.builder()
                .username(dto.getUsername())
                .password(dto.getPassword()) // 注意：需要在Service层加密
                .email(dto.getEmail())
                .phone(dto.getPhone())
                .realName(dto.getRealName())
                .gender(dto.getGender())
                .birthDate(dto.getBirthDate())
                .age(dto.getAge())
                .country(dto.getCountry())
                .city(dto.getCity())
                .bio(dto.getBio())
                .hobbies(dto.getHobbies())
                .newsletterSubscription(dto.getNewsletterSubscription())
                .termsAccepted(dto.getTermsAccepted())
                .build();
    }

    /**
     * Entity转响应DTO
     */
    public RealUserResponseDTO toResponseDTO(RealUser user) {
        return RealUserResponseDTO.builder()
                .id(user.getId())
                .username(user.getUsername())
                .email(user.getEmail())
                .phone(user.getPhone())
                .realName(user.getRealName())
                .gender(user.getGender())
                .birthDate(user.getBirthDate())
                .age(user.getAge())
                .country(user.getCountry())
                .city(user.getCity())
                .bio(user.getBio())
                .hobbies(user.getHobbies())
                .newsletterSubscription(user.getNewsletterSubscription())
                .registerDate(user.getRegisterDate())
                .build();
        // 注意：不返回密码！
    }

    /**
     * 更新DTO应用到Entity
     */
    public void updateEntity(RealUserUpdateDTO dto, RealUser user) {
        // 只更新非空字段
        if (dto.getPassword() != null && !dto.getPassword().isEmpty()) {
            user.setPassword(dto.getPassword());
        }
        if (dto.getEmail() != null) {
            user.setEmail(dto.getEmail());
        }
        if (dto.getPhone() != null) {
            user.setPhone(dto.getPhone());
        }
        if (dto.getRealName() != null) {
            user.setRealName(dto.getRealName());
        }
        if (dto.getGender() != null) {
            user.setGender(dto.getGender());
        }
        if (dto.getBirthDate() != null) {
            user.setBirthDate(dto.getBirthDate());
        }
        if (dto.getAge() != null) {
            user.setAge(dto.getAge());
        }
        if (dto.getCountry() != null) {
            user.setCountry(dto.getCountry());
        }
        if (dto.getCity() != null) {
            user.setCity(dto.getCity());
        }
        if (dto.getBio() != null) {
            user.setBio(dto.getBio());
        }
        if (dto.getHobbies() != null) {
            user.setHobbies(dto.getHobbies());
        }
        if (dto.getNewsletterSubscription() != null) {
            user.setNewsletterSubscription(dto.getNewsletterSubscription());
        }
    }
}
